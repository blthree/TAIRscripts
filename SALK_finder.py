import pandas as pd
from tinydb import TinyDB, Query
'''This script will can build and query a database of T-DNA insertions, built from the GBrowse track on TAIR'''

data_filename = 'data/tDNAs.gff3'


def create_db(filename, db_filename):
    db = TinyDB('tdna_db.json')
    df = pd.read_csv(filename, sep='\t', header=None, comment='#')
    df.drop([1, 2, 5, 6, 7], axis=1, inplace=True)
    df.columns = ['chr', 'start', 'end', 'info']
    df['name'] = df['info'].str.split(';', expand=True)[0]
    df.drop(['info'], axis=1, inplace=True)
    df.replace(['Name=', 'Chr'], '', inplace=True, regex=True)
    #df.set_index('name', drop=True, inplace=True)
    jason = df.to_json(orient='records')
    savef = open(db_filename, 'w')
    savef.write(jason)
    return
#create_db(data_filename, 'db/tdna_db.json')
# load the database
db = TinyDB('db/testdb.json')
#new_search = Query()
#db


