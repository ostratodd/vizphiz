import re
import argparse 

ap = argparse.ArgumentParser(description='Converts FASTA file to TSV format.')
ap.add_argument("-in", "--input_file", default=True, 
        help="input FASTA file")
ap.add_argument("-ot", "--output_file", default=True, 
        help="output text file")
args = vars(ap.parse_args())
input = args["input_file"]
output = args["output_file"]

file1 = open(input, 'r') 
file2 = open(output, 'a+')
lines = file1.readlines()
line_count = len(lines)
tab_entry = ""
i = 0
k = 0
loop = range(9)

for line in lines:

    for entries in loop:

        line1 = str(lines[k])
        line1 = line1.lstrip().replace("\n","")   
        if k == i:
            tab_entry = str(line1) + "\n"

        else:
            tab_entry = tab_entry + str(line1)
            tab_entry.rstrip()
        k+=1

    file2.write(tab_entry + "\n")
        
    tab_entry = ""
    #I want code to read two lines at a time, replace any ">" with empty sapce and any new lines with a tab instead
    i+=9
    k = i 

    if i >= line_count:
        break


file1.close()
file2.close()

