
data_filenames = ['data/T-DNA.salk.tab', 'data/T-DNA.sail.tab', 'data/T-DNA.gk.tab']
# http://signal.salk.edu/database/transcriptome/AT9.fa
# http://signal.salk.edu/database/transcriptome/T-DNA.SALK
# The +/+ strand is 'W' on SALK data and +/- is 'C'

def load_data(filenames):
    assert type(filenames) == list, "Filenames must be in the form of a list"
    records = {}
    f_out = open('data/condensed.tab', 'w')
    for fname in filenames:
        f = open(fname, 'r')
        # parsing logic
        for line in f:
            s_line = line.strip('\n').split('\t')
            stock_name = s_line[0].split('.')[0]
            poly_num = str(s_line[0][11:])
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
            poly_len = str(int(poly_end) - int(poly_start))
            # save data without un-needed info
            stock_name = stock_name.replace('SALK', 'SK')
            stock_name = stock_name.replace('SAIL', 'SL')
            line_out = "\t".join([stock_name, poly_num, poly_chr, orientation, poly_start, poly_len])
            f_out.write(line_out + '\n')

        f.close()
    f_out.close()
    return records

db = load_data(data_filenames)
print(db.get('SALK_001127'))








