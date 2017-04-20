import pandas as pd
from tinydb import TinyDB, Query
import requests
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
#db = TinyDB('db/testdb.json')
#db.insert({'name':'SALK_111110', 'chr': '2', 'start': '234', 'end': '243'})
#new_search = Query()
#c = db.search(new_search.name == 'GK-887B01-030271')
#print(db.all())

url = 'http://www.arabidopsis.org/servlets/TairObject?name=SALK_105972.55.50.X&type=polyallele'
url2 = 'http://www.arabidopsis.org/servlets/TairObject?name=SALK_069069.23.60.x&type=polyallele'
r = requests.get(url2)

find_string = 'nuc_sequence</td>\n                <td class="sm">'
i_start = r.text.index('nuc_sequence</td>\n                <td class="sm">')
i_start += len(find_string) + 1
i_end = r.text[i_start:i_start+200].index('</td>')
print(i_end)
print(r.text[i_start:i_start+i_end])
#print(r.text)
#nuc_sequence</td>
#                <td class="sm">