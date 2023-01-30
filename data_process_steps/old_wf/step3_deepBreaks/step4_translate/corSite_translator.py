import argparse
import re #regular expressions

ap = argparse.ArgumentParser(description='Mutagenesis changes protein sequences with mutations named in the standard way')
ap.add_argument("-cs", "--correlated_sites", required=True, 
        help="The important sites highlighted by the deepBreaks program. Seperate by commas.")
ap.add_argument("-ot", "--output_file", default=True, 
        help="output text file")
ap.add_argument("-v", "--verbose", required=False, default="no", 
        help="-v yes will print more information")
args = vars(ap.parse_args())
impsites = args["correlated_sites"]
v = args["verbose"]
output = args["output_file"]
seq = input("Enter Aligned Bovine Sequence: ")
site_list = impsites.split('-')

#take the list of important sites and translate them to the bovine standard equivalent, we do this by taking the site number and subtracting the number of '-' between the start of the sequence and the desired site. 
for sites in site_list:
    cor_sites = str(sites).split(',')
    m = 0
    for site in cor_sites:    
        k = int(site)    
        gaps = seq[:k].count('-')
        #print("The number of gaps is " + str(gaps))
        trans_site = k - gaps

        with open(output, 'a') as f:
                if m == 0:
                        f.write("The following set of correlated sites have been translated to the standard Bovine equivalent...\n")   
                        m+=1 
                f.write(f"Site {k} == {trans_site}\n")       


