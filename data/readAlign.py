from Bio import AlignIO

alignment = AlignIO.read(open("yokoyamaPNAS2.nex"), "nexus")
print("Alignment length %i" % alignment.get_alignment_length())
for record in alignment:
    print(">"+record.id + "\n" + record.seq)
