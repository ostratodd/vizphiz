import argparse
import re #regular expressions

ap = argparse.ArgumentParser(description='Converts a 3-column table to LATEX to format species based on columns')
ap.add_argument("-f", "--filein", required=True, 
        help="In file in 3-column tab-delimited format")
args = vars(ap.parse_args())
infile = args["filein"]

#read file for data
file1 = open(infile, 'r')
Lines = file1.readlines()

count=0
for line in Lines:
    columns = line.split("\t")

    print(columns[0])
