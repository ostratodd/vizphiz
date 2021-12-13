# Import libraries
from Bio import pairwise2
from Bio.Seq import Seq
from Bio import Align
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
  
# Creating sample sequences
#NP_001014890.1
#bovine = seqRecord(Seq("MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDEASTTVSKTETSQVAPA", generic_protein), id="Bovine_rhodopsin_NP_001014890.1"))
#wt = seqRecord(Seq("MNGTEGQDFYIPMSNKTGIVRSPFEYPQYYLAEPWQYSVLAAYMFMLIMLGFPINFLTLYVTIQHKKLRTPLNYILLNLAFANHFMVLGGFTTTLYTSLHGYFVFGPTGCNIEGFFATLGGEIALWSLVVLAIERYIVVCKPMSNFRFGENHAIMGVTFTWIMALACAFPPLVGWSRYIPEGMQCSCGIDYYTLKPEVNNESFVIYMFVVHFTIPMTIIFFCYGRLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSNFGPIFMTAPAFFAKSSAIYNPVIYIMMNKQFRNCMLTTICCGKNPLGDDEASATASKTEQSSVSTSQVSPA", generic_protein), id = "wt"))

bovine = Seq("MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDEASTTVSKTETSQVAPA")
wt = Seq("MNGTEGQDFYIPMSNKTGIVRSPFEYPQYYLAEPWQYSVLAAYMFMLIMLGFPINFLTLYVTIQHKKLRTPLNYILLNLAFANHFMVLGGFTTTLYTSLHGYFVFGPTGCNIEGFFATLGGEIALWSLVVLAIERYIVVCKPMSNFRFGENHAIMGVTFTWIMALACAFPPLVGWSRYIPEGMQCSCGIDYYTLKPEVNNESFVIYMFVVHFTIPMTIIFFCYGRLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSNFGPIFMTAPAFFAKSSAIYNPVIYIMMNKQFRNCMLTTICCGKNPLGDDEASATASKTEQSSVSTSQVSPA")
  
##This works to align 2 seqs and print it
aligner = Align.PairwiseAligner()
alignments = aligner.align(bovine, wt)
print("Number of alignments: %d" % len(alignments))
alignment = alignments[0]
print(alignment)
print(alignment.target)
print(alignment.query)
print(alignment.score)
print(alignment.shape)
