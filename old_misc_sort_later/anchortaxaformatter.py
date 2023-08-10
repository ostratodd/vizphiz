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

    species = columns[0].strip()
    reason1 = columns[1].strip()
    reason2 = columns[2].strip()
    reason3 = columns[3].strip()
    access = columns[4].strip()

    #Find color based on access
    color = "\color{black}"
    if(access == "Lab cultures or for purchase"):
        color = "\color{purple}"
    if(access == "Expected on GoM or Arctic Cruise"):
        color = "\color{blue}"
    if(access == "Collecting local to LITE-MAR participant"):
        color = "\color{teal}"
    if(access == "Colleague will provide"):
        color = "\color{orange}"

    #Create superscripts
    superscripts = []
    if(reason1 == "Extensive physiology data exists") :
        superscripts.append("1")
    if(reason1 == "Extensive genomic data exists") :
        superscripts.append("2")
    if(reason1 == "Special trait (e.g. eye or bioluminescence)") :
        superscripts.append("3")
    if(reason1 == "Phylogenetic position") :
        superscripts.append("4")
        
    if(reason2 == "Extensive physiology data exists") :
        superscripts.append("1")
    if(reason2 == "Extensive genomic data exists") :
        superscripts.append("2")
    if(reason2 == "Special trait (e.g. eye or bioluminescence)") :
        superscripts.append("3")
    if(reason2 == "Phylogenetic position") :
        superscripts.append("4")
        
    if(reason3 == "Extensive physiology data exists") :
        superscripts.append("1")
    if(reason3 == "Extensive genomic data exists") :
        superscripts.append("2")
    if(reason3 == "Special trait (e.g. eye or bioluminescence)") :
        superscripts.append("3")
    if(reason3 == "Phylogenetic position") :
        superscripts.append("4")
        
    joinedss = ",".join(superscripts)
    print(color + " \emph{" + species + "}" + "$^{" + joinedss + "}$" + "\color{black}, ")
