from linecache import getline
import primer3

data_filename = 'data/T-DNA.salk.tab'

def load_data(filename):
    f = open(filename, 'r')
    records = {}
    for line in f:
        s_line = line.strip('\n').split('\t')
        poly_name = s_line[0]
        poly_chr, poly_loc = s_line[1].split(':')
        poly_chr = poly_chr[3:]
        poly_loc = int(poly_loc)
        orientation = s_line[3].split('/')[0]
        # load into dict of dicts object
        records[poly_name] = {'name':poly_name, 'chr':poly_chr, 'orientation':orientation, 'location':poly_loc}
    return records

def extract_sequence(chr, location, upstream_dist=0, downstream_dist=0):
    # SALK_058673.44.55.x	chr2:011164117	1e-18	W/11164117-11164162
    filename = 'chr' + str(chr) + '.fa'
    # calculate line number, add one line since fasta file has a header
    # and another line to account for zero-indexed numbering of linecache.getline()
    line_no = int(location / 60) + 2
    # calculate the exact location of the insertion on the line
    char_no = location % 60
    result = getline(filename, line_no).strip('\n')
    return result

extract_sequence(2,11164117)