import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


base_url = r'C:\Users\anees.hussain\OneDrive - Accenture\Downloads\names'

# names1880 = pd.read_csv(r'C:\Users\anees.hussain\OneDrive - Accenture\Downloads\names\yob1880.txt', names=['name', 'sex', 'births'])

names1880 = pd.read_csv(base_url + '\yob1880.txt', names=['name', 'sex', 'births'])

# print(names1880)

# print(names1880.groupby('sex').births.sum())

years = range(1880, 2023)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = '\yob%d.txt' % year
    frame = pd.read_csv(base_url + path, names=columns)

    frame['year'] = year
    pieces.append(frame)

    names = pd.concat(pieces, ignore_index=True)

# print(names)

# total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# print(total_births)

total_births.tail()

total_births.plot(title='Total births by sex and year')

def add_prop(group):
    births = group.births.astype(float)

    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

