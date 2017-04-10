import requests
from bs4 import BeautifulSoup
import re
#soup = BeautifulSoup(html_doc, 'html.parser')

locus_AGI = "AT1G02850"

base_url = 'http://www.arabidopsis.org/servlet/Search?type=dna&action=search'
general_fields = {'pageNum': '1', 'search': 'Submit+Query', 'dna_type': 'clone',
                  'type_1': 'locus', 'method_1': '2', 'term_1': 'AT1G02850', 'other_features': 'is_abrc_stock'}

search_results = requests.get(base_url, params=general_fields)
# load the results page into the html parser
results = BeautifulSoup(search_results.text, 'html.parser')
# get all rows from tables on the page
t_rows = results.find_all('tr')

# iterate thru rows to find the rows with available clones
clone_links = {}
for r in t_rows:
    rl = r.find('a')
    # find all checkboxes on the line. Stocks that are available will have 2 checkboxes
    r_checkbox = r.find_all('input')
    # test that there's a link to a clone and the stock has 2 checkboxes, i.e. available
    if rl is not None and 'servlets' in rl.get('href') and len(r_checkbox) == 2:
        # clone_links format {clone name: relative link to clone}
        clone_links[rl.text.strip('\xa0')] = rl.get('href')

# remove CATMA clones
remove_clones = []
for k in clone_links.keys():
    if k.startswith('CATMA'):
        remove_clones.append(k)
for k in remove_clones:
    clone_links.pop(k)
print(clone_links.keys())

all_fields = ['pageNum=1', 'search=Submit+Query', 'dna_type=clone', 'taxon=', 'type_1=locus', 'method_1=2', 'term_1=AT1G02850', 'type_2=clone', 'method_2=2', 'term_2=', 'type_3=stock_number', 'method_3=2', 'term_3=', 'vector_type=plasmid', 'insert_type=cDNA', 'clone_end_type=any', 'other_features=is_abrc_stock', 'chromosome=', 'map_type=', 'range_type=between', 'low_range=', 'low_unit=none', 'high_range=', 'high_unit=none', 'size=25', 'order=name']



