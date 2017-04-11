import requests

r = requests.get('http://www.arabidopsis.org/servlets/TairObject?type=sequence&id=2002962550')
f = open('tair-dump.txt', mode='w')
f.write(r.text)

'''https://www.arabidopsis.org/servlets/Search?type=general&search_action=detail&method=1&show_obsolete=F&name=AT1g02850&sub_type=gene&SEARCH_EXACT=4&SEARCH_CONTAINS=1
'''

'''
found seq in 2 places: the actual sequence displayed, and the send to wu-blast button

Display Sequence:
<td class="sm" ><p style="font-family: monospace">

  &nbsp;&nbsp;&nbsp;1&nbsp;ACCGTT


WUBLAST button:
<form action="/wublast/index2.jsp" method="post">
        <input type="hidden" name="sequence" value="ACCG
'''

begin_index = r.text.index('name="sequence" value=')
end_index = r.text.index('" />\n\t    <input type="hidden" name="sequence_type" value="nucleotide" />')
sequence = r.text[begin_index + 23:end_index]
sequence = sequence.replace('\n', '').replace('\r', '') # not needed but keep for now to match _yeast.py
print('seq is:')
print(sequence[:10])

