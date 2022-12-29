import argparse
import re #regular expressions

ap = argparse.ArgumentParser(description='Mutagenesis changes protein sequences with mutations named in the standard way')
ap.add_argument("-is", "--impsite", required=True, 
        help="The important sites highlighted by the deepBreaks program. Seperate by commas.")
ap.add_argument("-ts", "--target_sequence", required=False, 
        help="The bovine sequence aligned for the database.")
ap.add_argument("-v", "--verbose", required=False, default="no", 
        help="-v yes will print more information")
args = vars(ap.parse_args())
impsites = args["impsite"]
seq  = args["target_sequence"]
v = args["verbose"]

seq = "---M-----------------------------NGTE-----------GPNFYVP----FSNKTGVVRSPF------------------EAPQY-YLAEPWQ---FSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTG-CNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVG-WSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCY-GQLVFTVKEAAAQQQE--------------SATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDE--ASTT-V-SKT-E--------T--------SQVAPA---------------"

site_list = impsites.split(',')

#take the list of important sites and translate them to the bovine standard equivalent, we do this by taking the site number and subtracting the number of '-' between the start of the sequence and the desired site. 
for sites in site_list:

    k = int(sites)    
    gaps = seq[:k].count('-')
    #print("The number of gaps is " + str(gaps))
    trans_site = k - gaps

    print(f"For site {k} the bovine equivalent is {trans_site}") 


