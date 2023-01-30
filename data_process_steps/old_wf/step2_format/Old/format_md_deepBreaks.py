import pdb
from numpy import array
import numpy
import pandas as pd
m = 0
k = 1
def convert_list_to_string(org_list, seperator=' '):

    return seperator.join(org_list)


meta_fields = ['AA_Seq']
meta_data = pd.read_csv('tab_aligned_phylip.txt', sep='\t', usecols=meta_fields)

meta_data.to_csv(r'placeholder.txt', index=None, sep='\t', mode='a')
file1 = open('placeholder.txt', 'r')
file2 = open('sd1.txt', 'a')

for lines in file1:
    

    if m == 0:
        while k <= 470:
            pos = f"\tp{str(k)}"
            k+=1
            file2.write(pos)
        file2.write("\n")
    else:
        arr = list(lines)
        #print(arr)
        full_str = convert_list_to_string(arr, '\t')
        seq = '>S'+ str(m) + '\t' + full_str
        file2.write(seq)

    m+=1

file1.close()
