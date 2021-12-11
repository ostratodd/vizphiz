from Bio import Entrez, SeqIO
Entrez.email = 'oakley@ucsb.edu'
handle = Entrez.efetch(db="nucleotide", id="U57536", rettype="gb", retmode="text")
record = SeqIO.read(handle, "gb")
handle.close()
id = record.id
dna = record.seq
organism = record.annotations["organism"]
orglist = organism.split(" ")
genus = orglist[0]
species = orglist[1]

for i,feature in enumerate(record.features):
     if feature.type=='CDS':
          aa = feature.qualifiers['translation'][0]

print(genus, end='\t')
print(species, end='\t')
print(id, end='\t')
print(dna, end='\t')
print(aa, end='\n')

