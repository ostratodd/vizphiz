import pdb 
from Bio import AlignIO
import numpy as np
import numpy
import pandas as pd
from scipy import spatial

aln = np.array(open('tab_aligned_phylip.txt', 'r'))
print(aln)

d_matrix = spatial.distance_matrix(aln, aln, p=2)
print(d_matrix)

