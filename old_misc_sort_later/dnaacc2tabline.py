from Bio import Entrez, SeqIO
Entrez.email = 'oakley@ucsb.edu'

# Using readlines()
file1 = open('accessions.txt', 'r')
Lines = file1.readlines()
 
# Strips the newline character
for line in Lines:
    acc = line.strip()
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text")
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
    print("NCBI", end='\t')
    print(id, end='\t')
# Comment one of next two lines to print or to not print DNA right now
    print(dna, end='\t')
#    print(end='\t')
    print(aa, end='\n')
#    print(" ")
