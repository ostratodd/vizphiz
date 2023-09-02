import pdb
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from numpy import array
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
import matplotlib 
import matplotlib.pyplot as plt

aln = AlignIO.read(open('phylip_4_matrix.phylip'),'phylip')
print(aln)

calculator = DistanceCalculator('blosum62')

file1 = open('opsin_seq_distance_matrix.txt', 'a')

dm = (str(calculator.get_distance(aln)))

constructor = DistanceTreeConstructor(calculator)

phylo_tree = constructor.build_tree(aln)
phylo_tree.rooted = True

#Phylo.write(phylo_tree, "opsin_phylo.xml", "phyloxml")

fig = Phylo.draw(phylo_tree)
print(fig)
