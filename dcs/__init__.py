import os
import pandas as pd
from pprint import pprint

location = os.path.dirname(os.path.realpath(__file__))

data = {}

for file in os.listdir(os.path.join(location, 'data')):
    filename = file.split('.')[0]
    data[filename] = file

def list_datasets():
    pprint(data)


def load(filename):
    """
    Loads one of the datasets used in DCSS.
    """
    datapath = os.path.join(location, 'data', data[filename])
    df = pd.read_csv(datapath, low_memory=False)
    return df

def load_vdem():
    """
    Loads the full V-DEM 10 dataset.
    """
    dfs = []
    for file in os.listdir(os.path.join(location, 'data')):
        datapath = os.path.join(location, 'data', file)
        df = pd.read_csv(datapath, low_memory=False)
        dfs.append(df)
    df = pd.concat(dfs)
    return df
    

