import argparse
import re #regular expressions

ap = argparse.ArgumentParser(description='Mutagenesis changes protein sequences with mutations named in the standard way')
ap.add_argument("-is", "--impsite", required=True, 
        help="The important sites highlighted by the deepBreaks program. Seperate by commas.")
ap.add_argument("-ot", "--output_file", default="impsite_translated.txt", 
        help="output text file")
ap.add_argument("-v", "--verbose", required=False, default="no", 
        help="-v yes will print more information")
args = vars(ap.parse_args())
impsites = args["impsite"]
v = args["verbose"]
output = args["output_file"]
seq = input("Enter Aligned Bovine Sequence: ")
site_list = impsites.split(',')
m = 0

#take the list of important sites and translate them to the bovine standard equivalent, we do this by taking the site number and subtracting the number of '-' between the start of the sequence and the desired site. 
for sites in site_list:

    k = int(sites)    
    gaps = seq[:k].count('-')
    #print("The number of gaps is " + str(gaps))
    trans_site = k - gaps

    print(f"For site {k} the bovine equivalent is {trans_site}") 

    with open(output, 'a') as f:
        if m == 0:
                f.write("The following sites have been translated to the standard Bovine equivalent...\n")   
                m+=1 
        f.write(f"Site {k} == {trans_site}\n")       


