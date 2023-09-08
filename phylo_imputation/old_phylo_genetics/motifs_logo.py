import pdb 
from Bio import motifs
import numpy
import pandas as pd
from scipy.spatial import distance_matrix
from skbio.stats.distance import DistanceMatrix
m = 0

data = ['ID','AA_Seq']
file1 = pd.read_csv('tab_aligned_phylip.tsv', sep='\t', usecols=data)
#print(file1)

acc_list = file1['ID'].values.tolist()
#print(acc_list)

data_list = file1['AA_Seq'].values.tolist()
print(data_list)

motif = motifs.create(data_list)
motif.weblogo('giant_motif1.pdf',format = 'pdf')






        

