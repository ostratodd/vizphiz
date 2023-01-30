import pdb
from numpy import array
import numpy
import pandas as pd
m = 0

meta_fields = ['Accession','Species','Gene_Family','Lambda_Max']
meta_data = pd.read_csv('fixed_opsins_aligned2.tsv', sep='\t', usecols=meta_fields)

meta_data.to_csv(r'meta_data.txt', index=None, sep='\t', mode='a')
file1 = open('meta_data.txt', 'r')
file2 = open('meta_data_formatted2.txt', 'a')

for lines in file1:
    
    if m == 0:
        seq = '\t' + lines.replace('\t','|',2)
        file2.write(seq)
    else:
        seq = 'S'+ str(m) + '\t' + lines.replace('\t','|',2)
        file2.write(seq)

    m+=1

file1.close()
