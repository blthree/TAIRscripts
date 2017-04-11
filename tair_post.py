import requests
import re

'''payload options
datasets: ATH1_cds, ATH1_seq, AT_transcripts
search_against: gene_model, rep_gene
'''


def fetch_arabidopsis_locus_sequence(locus_name, seq_dataset='ATH1_cds', dump=False):
    payload = {'loci': locus_name, 'dataset': seq_dataset, 'search_against': 'rep_gene'}
    r = requests.post('https://www.arabidopsis.org/cgi-bin/bulk/sequences/getseq.pl', data=payload)
    begin_index = r.text.index('LENGTH=')
    sequence = r.text[begin_index + 7:]
    sequence = re.sub(r'\d', '', sequence).replace('\n', '').replace('\r', '')
    if dump:
        f = open('tair-dump.txt', 'w')
        f.write(r.text)
    return sequence


def fetch_arabidopsis_clone_sequence(clone_name, seq_dataset='ATH1_cds', dump=False):
    payload = {'dna_type':'clone', 'type_1':'clone', 'method_1':'exactly', 'term_1': clone_name, 'vector_type': 'plasmid', 'insert_type': 'cDNA', 'other_features': 'is ABRC stock'}
    r = requests.post('https://www.arabidopsis.org/cgi-bin/bulk/sequences/getseq.pl', data=payload)
    begin_index = r.text.index('LENGTH=')
    sequence = r.text[begin_index + 7:]
    sequence = re.sub(r'\d', '', sequence).replace('\n', '').replace('\r', '')
    if dump:
        f = open('tair-dump.txt', 'w')
        f.write(r.text)
    return sequence

def get_clone_insert(clone_name):
    # define urls we will use
    # eventually should just make general search function
    # then we can pass search parameters to the function instead of hardcoding them
    base_url = 'https://www.arabidopsis.org'
    search_url = '/servlet/Search?type=dna&action=search&pageNum=1&dna_type=clone&taxon=' \
                 '&type_1=clone&method_1=4&term_1='\
                 + clone_name + \
                 '&type_2=accession&method_2=2&term_2=&type_3=stock_number&method_3=2' \
                 '&term_3=&vector_type=plasmid&insert_type=' \
                 'cDNA&clone_end_type=any&other_features=is_abrc_stock&chromosome=&map_type=' \
                 '&range_type=between&low_range=&low_unit=' \
                 'none&high_range=&high_unit=none&size=25&order=name&search=Submit+Query'

    r = requests.get(base_url + search_url)

    # find table element with link to clone (clone here is U09681)
    # <td class="sm"><a href="/servlets/TairObject?id=500939579&type=clone">U09681&nbsp;</a></td>
    begin_name_index = r.text.index('/servlets/TairObject?id=')
    end_name_index = r.text.index('">' + clone_name + '&nbsp')
    path_to_clone_page = r.text[begin_name_index:end_name_index]
    #print(path_to_clone_page)
    #f = open('tair-dump.txt', 'w')
    #f.write(r.text)


        # get clone page
    r = requests.get(base_url + path_to_clone_page)
    # find table element with link to insert sequence
    # type=sequence&id=
    begin_seq_index = r.text.index('/servlets/TairObject?type=sequence&id=')
    end_seq_index = r.text.index('">cDNA</a')
    path_to_seq_page = r.text[begin_seq_index:end_seq_index]
    print(path_to_seq_page)

    # get sequence page
    r = requests.get(base_url + path_to_seq_page)
    begin_index = r.text.index('name="sequence" value=')
    end_index = r.text.index('" />\n\t    <input type="hidden" name="sequence_type" value="nucleotide" />')
    sequence = r.text[begin_index + 23:end_index]
    sequence = sequence.replace('\n', '').replace('\r', '')  # not needed but keep for now to match _yeast.py
# TODO: add some actual error handling


    return sequence


