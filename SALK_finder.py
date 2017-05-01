import pandas as pd
from tinydb import TinyDB, Query
import requests
'''This script will can build and query a database of T-DNA insertions, built from the GBrowse track on TAIR'''

data_filename = 'data/T-DNA.salk.tab'

df = pd.read_csv(data_filename, sep='\t', header=None)
df = pd.concat([df, df[3].str.split('/', expand=True)], axis=1)

df.columns = ['name', 'chr', 'eval', 'delete_this', 'orientation', 'coords']
df.drop(['eval', 'delete_this'], axis=1, inplace=True)
temp = df['chr'].str.split(':')
df['chr'] = temp.str[0]
print(df.head())