import os
import sys
import torch
import pickle
from internetarchive import get_item

__version__ = "0.0.1"
__author__ = "Tung Nguyen, Hritik Bansal, Shashank Goel"
__credits__ = "University of California, Los Angeles"
    
class ClimateDataset:
    areas = {
        "germany": {
            "TEST_LEN": 2922,
            "NUM_TRAIN_STATIONS": 40
        }
    }  
    
    def __init__(self, root: str, area: str, train: bool = True, temporal_context: bool = False, temporal_target: bool = False, history_len: int = 5, offset: int = 1):
        area_file_path = self.setup(root, area)
            
        with open(area_file_path, "rb") as file:
            context, target = pickle.load(file)
            self.context, self.target = torch.from_numpy(context), torch.from_numpy(target)
        
        finite = list(map(lambda x: torch.isfinite(x).any(), self.context))
        self.context, self.target = self.context[finite], self.target[finite]

        if(temporal_context): self.context = self.construct_temporal(self.context, history_len, offset)
        if(temporal_target): self.target = self.construct_temporal(self.target, history_len, offset)
            
        if(temporal_context or temporal_target):
            len_context, len_target = self.context.shape[0], self.target.shape[0]
            self.context, self.target = self.context[-len_target:], self.target[-len_context:]

        TEST_LEN = ClimateDataset.areas[area]["TEST_LEN"]
        NUM_TRAIN_STATIONS = ClimateDataset.areas[area]["NUM_TRAIN_STATIONS"]
        
        if(train):
            self.context = self.context[:-TEST_LEN]
            self.target = self.target[:-TEST_LEN, :NUM_TRAIN_STATIONS] if not temporal_target else self.target[:-TEST_LEN, :, :NUM_TRAIN_STATIONS]
        else:
            self.context = self.context[-TEST_LEN:]
            self.target = self.target[-TEST_LEN:, NUM_TRAIN_STATIONS:] if not temporal_target else self.target[-TEST_LEN:, :, NUM_TRAIN_STATIONS:]        

    def construct_temporal(self, x, history_len, offset):
        x = x.unsqueeze(0).repeat_interleave(history_len + 1, dim=0)
        for i in range(history_len):
            x[i] = torch.roll(x[i], shifts = -i, dims = 0)
        x[history_len] = torch.roll(x[history_len], shifts = -(history_len + offset - 1), dims = 0)
        x = x[:, :-(history_len + offset - 1)]
        x = torch.transpose(x, dim0 = 0, dim1 = 1)
        return x

    def construct_yearly(self, context, leng):
        dpy = 365
        rows = len(context) - dpy * leng
        yearly_context = []
        for i in range(rows):
            yearly_context.append(context[i:i + dpy * leng + 1:dpy])
        yearly_context = torch.stack(yearly_context, dim = 0)
        return yearly_context
    
    def __getitem__(self, index):
        return (self.context[index], self.target[index])
    
    def setup(self, root, area):
        os.makedirs(root, exist_ok = True)
        area_file_path = os.path.join(root, f"{area}.pt")

        if(not os.path.exists(area_file_path)):
            item = get_item("clidow")
            file = item.get_file(f"{area}.pt")
            file.download(area_file_path)   
        
        return area_file_path     
    
    def __len__(self):
        return self.context.shape[0]