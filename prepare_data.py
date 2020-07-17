# John McLevey 
# University of Waterloo 
# Summer 2020 

import pandas as pd

df = pd.read_csv('dcs/data/raw/V-Dem-CY-Full+Others-v10.csv', low_memory=False)

lc = df['country_name'].unique().tolist()

countries = df.groupby('country_name')

for country in lc:
    dataset_name = country.replace(' ', '_').replace('/','_')
    c = countries.get_group(country)
    c.to_csv(f'dcs/data/{dataset_name}.csv', index=False)
    print(f'Created the dataset for: {country}')



