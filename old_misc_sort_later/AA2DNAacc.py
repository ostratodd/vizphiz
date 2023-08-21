from Bio import Entrez, SeqIO
Entrez.email = 'oakley@ucsb.edu'

# Using readlines()
file1 = open('accessions.txt', 'r')
Lines = file1.readlines()
 
# Strips the newline character
for line in Lines:
    acc = line.strip()
    handle = Entrez.efetch(db="protein", id=acc, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "gb")
    handle.close()

    for i,feature in enumerate(record.features):
         if feature.type=='CDS':
              aa = feature.qualifiers['coded_by'][0]
    dna = aa.split(":")


    print(dna[0])
