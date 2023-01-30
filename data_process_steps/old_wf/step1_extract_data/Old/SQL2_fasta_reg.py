import argparse
import mysql.connector
import re


ap = argparse.ArgumentParser(description='Converts a 3-column table to LATEX to format species based on columns')
ap.add_argument("-ot", "--output_file", default=True, 
        help="output text file")
ap.add_argument("-md", "--metadata_file", default=True, 
        help="output metadata file")
args = vars(ap.parse_args())
output = args["output_file"]
metadata = args["metadata_file"]
m = 0
acc_list = []
duped = 0

#Heterologous starts here
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database=input("Database Name: "),
  password=input("Password: ")
)
mycursor = mydb.cursor()

sql = "select DISTINCT o.genus,o.species,o.genefamily,o.accession,h.lamdamax, o.aa from opsins.opsins o, opsins.heterologous h WHERE (o.accession = h.accession AND o.refid = h.refid); "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:      
  m += 1  
  #Keep all accessions in a list -- don't print 
  if (x[3] in acc_list):
    #print ("\n\n\n****Accession Exists" + x[2] + "\n\n" )
    duped=1
  #First 2 of if statements ignore ancestral (pigment named) or mutated genes
  if (duped==1) :
    duped=0
  #do not print if contains the word "pigment" which is an ancestral sequence
  
  else :
       with open(output, 'a') as f:
        seq = ">S" + str(m)
        f.write(seq)
        seq2 = str('\n' + x[5] + '\n')
        f.write(seq2)
       with open(metadata, 'a') as g:
        if m == 1:
          g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")  
        md =  str("S" + str(m) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
        g.write(md)
        