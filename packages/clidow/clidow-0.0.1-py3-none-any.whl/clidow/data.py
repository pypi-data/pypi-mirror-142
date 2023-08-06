https://drive.google.com/file/d/1NrEbW-6Gh8YIKrlE2ON1wQkhrL9QvQBK/view?usp=sharing

import os
import warnings
import xarray as xr
import numpy as np
import pickle
from torch.utils.data import Dataset
from einops import rearrange
import torch

warnings.filterwarnings("ignore")

TEST_LEN = 2922 # from 01/01/2011 to 12/31/2018
NUM_TRAIN_STATIONS = 40

def get_dataset(data_dir: str): 
    dataset = xr.open_mfdataset(f'{data_dir}/*.nc', combine = 'by_coords', compat = 'override')
    return dataset

def get_var_dict():
    return({'geopotential': ('z', [500, 700, 850]), 
            'temperature': ('t', [500, 700, 850]), 
            'u_component_of_wind': ('u', [500, 700, 850]), 
            'v_component_of_wind': ('v', [500, 700, 850]), 
            'specific_humidity': ('q', [500, 700, 850]), 
            '2m_temperature': ('t2m', None), 
            '10m_u_component_of_wind': ('u10', None), 
            '10m_v_component_of_wind': ('v10', None), 
            'total_precipitation': ('tp', None), 
            'constants': ['lat2d','lon2d','orography'],
            })

class DataGenerator(Dataset):
    def __init__(self, ds, var_dict, station_file = '', add_temporal_features = True, mean = None, std = None, 
                time_steps = 1, shuffle = True, tp_log = 0.01, norm_subsample = 30000, train=True):
        '''
            DataGenerator for Statistical downscaling in Climate regimes
            Args:
                ds: Dataset containing all variables
                var_dict: Dictionary of the form {'varname': ('var':[level1,..leveln])}. Use None if no level involved
                add_temporal_features: form of positional encoding for day of the year
                time_steps: How many time steps for input. After data_subsample
            ToDo:
                Add a support to include station data as well
            Output:
                tuple: ((batch_size, time x number of vars, lat, lon), 
                        (batch_size, lat_stations, lon_stations, max_temp, avg_ppt)
                        ) where batch_size represents different days
        '''

        self.ds = ds
        self.var_dict = var_dict
        self.add_temporal_features = add_temporal_features
        self.norm_subsample = norm_subsample
        self.time_steps = time_steps

        data = []
        level_names  = []
        generic_level = xr.DataArray([1], coords = {'level': [1]}, dims = ['level'])
        for long_var, params in self.var_dict.items():
            if long_var == 'constants':
                for var in params:
                    da = ds[var]
                    da = da.expand_dims({'level': generic_level, 'time': ds.time}, (1, 0))
                    da = da.assign_coords(sintime = ('time', ds.sintime.values), costime = ('time', ds.costime.values))
                    data.append(da)
                    level_names.append(var)
            else:
                var, levels = params
                da = ds[var]
                if tp_log and var == 'tp':
                    da = np.log(da + tp_log) - np.log(tp_log)
                try:
                    data.append(da.sel(level = levels))
                    level_names += [f'{var}_{level}' for level in levels]
                except:
                    data.append(da.expand_dims({'level': generic_level}, 1))
                    level_names.append(var)
        self.data = xr.concat(data, 'level').transpose('time', 'lat', 'lon', 'level')
        self.data['level_names'] = xr.DataArray(
            level_names, dims=['level'], coords = {'level': self.data.level}
        )

        try:
          self.const_idxs = [i for i, l in enumerate(self.data.level_names) if l in var_dict['constants']]
          self.not_const_idxs = [i for i, l in enumerate(self.data.level_names) if l not in var_dict['constants']]
        except:
          self.const_idxs = None
          self.not_const_idxs = [i for i, l in enumerate(self.data.level_names)]

        self.dt = self.data.time.diff('time')[0].values / np.timedelta64(1, 'h')
        self.dt_in = int(self.time_steps // self.dt)

        if mean is not None:
            self.mean = mean
        else:
            self.mean = self.data.isel(time=slice(0, None, norm_subsample)).mean(('time', 'lat', 'lon')).compute()
            if 'tp' in self.data.level_names:
                tp_idx = list(self.data.level_names).index('tp')
                self.mean.values[tp_idx] = 0
                
        if std is not None:
            self.std = std
        else:
            self.std = self.data.isel(time = slice(0, None, norm_subsample)).std(('time', 'lat', 'lon')).compute()
        
        if tp_log is not None:
            self.mean.attrs['tp_log'] = tp_log
            self.std.attrs['tp_log'] = tp_log
        
        ## Normalize
        self.data = (self.data - self.mean) / self.std
        if add_temporal_features:
            self.data = self.get_temporal_features()
            self.pos_idxs = [len(self.data['level_names']) - 2, len(self.data['level_names']) - 1]
        
        self.level_names = self.data['level_names']
        
        ## dissolve the dataset 
        ## reshape the data into per day basis
        self.data = self.data.values 
        ## (day, time, lat, lon, features)
        self.data = rearrange(self.data, '(d t) la lo v -> d t la lo v', t = 24)
        assert(self.time_steps <= 24)
        self.data = self.data[:, ::self.time_steps,:,:,:]

        self.station_data = np.load(station_file)
        assert(len(self.station_data) == len(self.data))
    
    def __getitem__(self, i):
        return (self.data[i], self.station_data[i])
    
    def __len__(self):
        return len(self.data)

    def get_temporal_features(self):
        day_sinpos = self.data.sintime.values
        day_cospos = self.data.costime.values
        time_pos = np.concatenate([np.expand_dims(day_sinpos, 1), np.expand_dims(day_cospos, 1)], axis = 1)
        lat, lon = self.data.shape[1], self.data.shape[2]
        res = np.concatenate([np.expand_dims(np.concatenate([np.full((1,lat,lon), t) for t in x], axis = 0), axis = 0) for x in time_pos])
        time_darr = xr.DataArray(res, dims=['time', 'level', 'lat', 'lon'], 
                    coords={'time':self.data.time.values, 'level':[1,1], 'lat':self.data.lat.values, 'lon':self.data.lon.values})

        time_darr['level_names'] = xr.DataArray(
            ['sinpos', 'cospos'], dims=['level'], coords={'level': [1,1]})
        
        return xr.concat([self.data, time_darr], 'level')


class ClimateDataset(Dataset):
    def __init__(self, data_path, train=True, temporal_context=False, temporal_target=False, history_len=10, offset=1):
        with open(data_path, 'rb') as f:
            data, station_data = pickle.load(f)
            self.data = torch.from_numpy(data)
            self.station_data = torch.from_numpy(station_data)
        
        self.remove_nan()

        if temporal_context:
            assert history_len > 1
            self.data = self.construct_temporal(self.data, history_len, offset)
            # self.data = self.construct_yearly(self.data, history_len)
        if temporal_target:
            assert history_len > 1
            self.station_data = self.construct_temporal(self.station_data, history_len, offset)
            # self.station_data = self.construct_yearly(self.station_data, history_len)
            
        if temporal_context or temporal_target:
            len_data, len_station_data = self.data.shape[0], self.station_data.shape[0]
            self.data = self.data[-len_station_data:]
            self.station_data = self.station_data[-len_data:]

        if train:
            self.data = self.data[:-TEST_LEN]
            self.station_data = self.station_data[:-TEST_LEN, :NUM_TRAIN_STATIONS] if not temporal_target \
                else self.station_data[:-TEST_LEN, :, :NUM_TRAIN_STATIONS]
        else:
            self.data = self.data[-TEST_LEN:]
            self.station_data = self.station_data[-TEST_LEN:, NUM_TRAIN_STATIONS:] if not temporal_target \
                else self.station_data[-TEST_LEN:, :, NUM_TRAIN_STATIONS:]

    def remove_nan(self):
        nan_ids = []
        for i in range(len(self.data)):
            if torch.isnan(self.data[i]).any():
                nan_ids.append(False)
            else:
                nan_ids.append(True)
        self.data = self.data[nan_ids]
        self.station_data = self.station_data[nan_ids]

    def construct_temporal(self, data, leng, offset):
        data = data.unsqueeze(0).repeat_interleave(leng+1, dim=0)
        for i in range(leng):
            data[i] = torch.roll(data[i], shifts=-i, dims=0)
        data[leng] = torch.roll(data[leng], shifts=-(leng+offset-1), dims=0)
        data = data[:, :-(leng+offset-1)]
        data = torch.transpose(data, dim0=0, dim1=1)
        return data

    def construct_yearly(self, data, leng):
        dpy = 365 # days per year
        rows = len(data) - dpy*leng
        yearly_data = []
        for i in range(rows):
            yearly_data.append(data[i:i+dpy*leng+1:dpy])
        yearly_data = torch.stack(yearly_data, dim=0)
        return yearly_data
    
    def __getitem__(self, index):
        return (self.data[index], self.station_data[index])

    def __len__(self):
        return self.data.shape[0]


# t_dataset = ClimateDataset("/u/scratch/s/shashank/shared/datasets/data_2_steps.pt", train=False, temporal_context=True, temporal_target=True, history_len=3, offset=4)
# print (t_dataset.data.shape)
# print (t_dataset.station_data.shape)
# dataset = ClimateDataset("/u/scratch/s/shashank/shared/datasets/data_2_steps.pt", train=False)
# print (dataset.data.shape)
# print (dataset.station_data.shape)

# data_1 = t_dataset[0][0]
# data_2 = torch.cat((dataset[:3][0], dataset[3+4-1][0].unsqueeze(0)), dim=0)
# print (data_1 == data_2)

# station_1 = t_dataset[0][1]
# station_2 = torch.cat((dataset[:3][1], dataset[3+4-1][1].unsqueeze(0)), dim=0)
# print (station_1 == station_2)