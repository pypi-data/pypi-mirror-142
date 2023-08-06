import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name = "clidow",
    version = "0.0.1",
    author = "Tung Nguyen, Hritik Bansal, Shashank Goel",
    author_email = "shashankgoel@ucla.edu",
    description = "Climate Downscaling Benchmarks",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/goel-shashank/CLIDOW",
    packages = setuptools.find_packages(),
    install_requires = [
        "torch",
        "pickle",
        "internetarchive",                   
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)