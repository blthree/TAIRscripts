
f = 'data/T-DNASeq.Genes.Araport11.txt'
f2 = 'data/TAIR9_GFF#_tdnas.gff'

def load_SALK_seq(filename):
    f = open(filename, 'r')
    records = {}
    for line in f:
        s_line = line.strip('\n').split('\t')
        stock_digits = s_line[0].split('_')[1].split('.')[0]
        poly_name = s_line[0]
        poly_chr = s_line[3]
        poly_locs = s_line[4].split(' ')[0]
        poly_start = poly_locs.split('-')[0]
        poly_gene = s_line[1].split('.')[0]
        # load into dict of dicts object
        if stock_digits in records:
            records[stock_digits][poly_name] = {'chr': poly_chr, 'gene': poly_gene, 'start': poly_start}
        else:
            records[stock_digits] = {poly_name: {'chr': poly_chr, 'gene': poly_gene, 'start': poly_start}}
    return records

def load_gff(filename):
    f = open(filename, 'r')
    records = {}
# Chr1	TAIR9	transposable_element_insertion_site	1	1	.	.	.	ID=Variation_SALK_001127.50.70.X.1_insertion;Name=SALK_001127.50.70.X.1
    for line in f:
        s_line = line.strip('\n').split('\t')
        poly_name = s_line[8].split('Name=')[1]
        stock_num = poly_name.split('.')[0]
        poly_chr = s_line[0]
        poly_start = s_line[3]
        poly_gene = s_line[1].split('.')[0]
        # load into dict of dicts object
        if stock_num in records:
            records[stock_num][poly_name] = {'chr': poly_chr, 'gene': poly_gene, 'start': poly_start}
        else:
            records[stock_num] = {poly_name: {'chr': poly_chr, 'gene': poly_gene, 'start': poly_start}}
    return records

records = load_SALK_seq(f)






