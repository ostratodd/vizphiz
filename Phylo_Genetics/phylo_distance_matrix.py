import pdb
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio import AlignIO
from numpy import array
import numpy
import pandas as pd


aln = AlignIO.read(open('phylip_4_matrix.phylip'),'phylip')
print(aln)

calculator = DistanceCalculator('blosum62')

file1 = open('opsin_seq_distance_matrix.txt', 'a')

file1.write(str(calculator.get_distance(aln)))

file1.close()