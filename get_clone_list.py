import requests

locus_AGI = "AT1G02850"

base_url = 'http://www.arabidopsis.org/servlet/Search?type=dna&action=search'
general_fields = []

'''&pageNum=1
&search=Submit+Query
&dna_type=clone
&taxon=
&type_1=locus
&method_1=2
&term_1=AT1G02850
&type_2=clone
&method_2=2&term_2=
&type_3=stock_number
&method_3=2
&term_3=
&vector_type=plasmid
&insert_type=cDNA
&clone_end_type=any
&other_features=is_abrc_stock
&chromosome=
&map_type=
&range_type=between
&low_range=
&low_unit=none
&high_range=
&high_unit=none
&size=25
&order=name'''


stuff = '&pageNum=1&search=Submit+Query&dna_type=clone&taxon=&type_1=locus&method_1=2&term_1=AT1G02850&type_2=clone&method_2=2&term_2=&type_3=stock_number&method_3=2&term_3=&vector_type=plasmid&insert_type=cDNA&clone_end_type=any&other_features=is_abrc_stock&chromosome=&map_type=&range_type=between&low_range=&low_unit=none&high_range=&high_unit=none&size=25&order=name'
split_stuff = stuff.split('&')
print(split_stuff)
