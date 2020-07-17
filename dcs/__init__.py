import os
import pandas as pd
from pprint import pprint

location = os.path.dirname(os.path.realpath(__file__))

data = {}

for file in os.listdir(os.path.join(location, 'data')):
    filename = file.split('.')[0]
    data[filename] = file

pprint(data)

# print(os.listdir(location))

# print(location)

# for f in :
#     print(f)

# data = {
#     'vdem':'V-Dem-CY-Full+Others-v10.csv'
# }

def load(dataset):
    """
    Loads one of the datasets used in DCSS.
    """
    datapath = os.path.join(location, 'data', data[dataset])
    df = pd.read_csv(datapath, low_memory=False)
    return df
