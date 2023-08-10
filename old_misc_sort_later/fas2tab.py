from Bio import SeqIO

decide = 1
for record in SeqIO.parse("rh1_12-13-21_ALN.fas", "fasta"):
    if decide == 1:
        #Here create tab file for R to do imputation
        print(record.id, end = "\t")
        counts = record.id.count("_")
        piece = record.id.split("_")
        print(piece[counts])
    
    else :
    #Below for simple tab delimted file shared with Crandall lab
        counts = record.id.count("_")
        piece = record.id.split("_")
        print(piece[2], end = "")
        if counts > 3:
            for x in range(counts-3):
                print("_" + piece[x+3], end = "")

        print("\t" + piece[0] + "_" + piece[1] + "\t" + piece[counts], end="\t")
        print(record.seq)
    
