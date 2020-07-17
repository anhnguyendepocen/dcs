import dcs 

# df = dcs.load('Ethiopia')
# print(df.sample(10))

df = dcs.load_vdem()
print(df.country_name.value_counts())