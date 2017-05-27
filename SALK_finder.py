from pyfaidx import Fasta
from primer3.bindings import designPrimers

data_filename = 'data/T-DNA.salk.tab'
# http://signal.salk.edu/database/transcriptome/AT9.fa
# http://signal.salk.edu/database/transcriptome/T-DNA.SALK

def load_data(filename):
    f = open(filename, 'r')
    records = {}
    for line in f:
        s_line = line.strip('\n').split('\t')
        poly_name = s_line[0]
        poly_chr = s_line[1].split(':')[0]
        poly_chr = poly_chr[3:]
        poly_start = s_line[3].split('/')[1].split('-')[0]
        poly_end = s_line[3].split('/')[1].split('-')[1]
        orientation = s_line[3].split('/')[0]
        # load into dict of dicts object
        records[poly_name] = {'name':poly_name, 'chr':poly_chr, 'orientation':orientation, 'start':poly_start, 'end':poly_end}
    return records



db = load_data(data_filename)
print(db.get('SALK_147584.18.15.x'))
genome = Fasta('AT9.fa')
print(genome.keys())
info = db.get('SALK_147584.18.15.x')
name = 'chr' + info['chr']
print(name)
print(genome[name][int(info['start']):int(info['end'])])
# still need to revcomp if reverse strand!

'''default iSECT values:
size: optimal=21 min=18 max=28
Tm: opt=61 Min=53 Max=71
%GC: min=20 max=80
clamp=1
maxN=300 ext5=300 ext3=300
primer_zone=200
BPos=110 (distance from LB primer to insertion site)
'''
