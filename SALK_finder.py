from pyfaidx import Fasta
from primer3.bindings import designPrimers

data_filename = 'data/T-DNA.salk.tab'
# http://signal.salk.edu/database/transcriptome/AT9.fa
# http://signal.salk.edu/database/transcriptome/T-DNA.SALK
# The +/+ strand is 'W' on SALK data and +/- is 'C'

def load_data(filename):
    f = open(filename, 'r')
    records = {}
    for line in f:
        s_line = line.strip('\n').split('\t')
        stock_name = s_line[0].split('.')[0]
        poly_name = s_line[0]
        poly_chr = s_line[1].split(':')[0]
        poly_chr = poly_chr[3:]
        poly_locs = s_line[3].split(',')[0]
        poly_start = poly_locs.split('/')[1].split('-')[0]
        poly_end = poly_locs.split('/')[1].split('-')[1]
        orientation = s_line[3].split('/')[0]
        # load into dict of dicts object
        if stock_name in records:
            records[stock_name][poly_name] = {'chr': poly_chr, 'orientation': orientation, 'start': poly_start, 'end': poly_end}
        else:
            records[stock_name] = {poly_name: {'chr': poly_chr, 'orientation': orientation, 'start': poly_start, 'end': poly_end}}
    return records



db = load_data(data_filename)
genome = Fasta('AT9.fa')
matches = db.get('SALK_054772')
p_first_name = list(matches.keys())[0]
print(p_first_name)
info = matches[p_first_name]
name = 'chr' + info['chr']
print(info['orientation'])
seq = genome[name][int(info['start']):int(info['end'])]

# still need to revcomp if reverse strand!


# upstream = maxN + Ext5 + primer_zone
# downstream = Ext3 + primer_zone
maxN = 300
ext5 = 300
ext3 = 300
p_zone = 200
bp_upstream = maxN + ext5 + p_zone
bp_downstream = ext3 + p_zone

if info['orientation'] == 'W':
    new_start = int(info['start']) - bp_upstream
    new_end = int(info['start']) + bp_downstream +1
    seq = genome[name][new_start:new_end]
    print(seq)
'''default iSECT values:
size: optimal=21 min=18 max=28
Tm: opt=61 Min=53 Max=71
%GC: min=20 max=80
clamp=1
maxN=300 ext5=300 ext3=300
primer_zone=200
BPos=110 (distance from LB primer to insertion site)
'''
print(len(str(seq)))
primer3_seq_args = {
        'SEQUENCE_ID': 'MH1000',
        'SEQUENCE_TEMPLATE': str(seq),
        #'SEQUENCE_EXCLUDED_REGION': [201,len(seq)-401],
        'SEQUENCE_PRIMER_PAIR_OK_REGION_LIST': [0, 200, 1100, 200]
    }
priner3_primer_args = {
        'PRIMER_OPT_SIZE': 21,
        'PRIMER_MIN_SIZE': 18,
        'PRIMER_MAX_SIZE': 28,
        'PRIMER_OPT_TM': 56.5,
        'PRIMER_MIN_TM': 51.0,
        'PRIMER_MAX_TM': 61.0,
        'PRIMER_MIN_GC': 20.0,
        'PRIMER_MAX_GC': 80.0,
        'PRIMER_MAX_POLY_X': 100,
        #'PRIMER_MAX_NS_ACCEPTED': 0,
        'PRIMER_MAX_SELF_ANY': 12,
        'PRIMER_MAX_SELF_END': 8,
        'PRIMER_PAIR_MAX_COMPL_ANY': 12,
        'PRIMER_PAIR_MAX_COMPL_END': 8,
        'PRIMER_PRODUCT_SIZE_RANGE': [1130,1140],
        'PRIMER_GC_CLAMP': 1,
        'PRIMER_THERMODYNAMIC_TEMPLATE_ALIGNMENT': 1,
        'PRIMER_MAX_TEMPLATE_MISPRIMING_TH': 46
    }
a = designPrimers(primer3_seq_args, priner3_primer_args)
for k,v in a.items():
    print(k,v)