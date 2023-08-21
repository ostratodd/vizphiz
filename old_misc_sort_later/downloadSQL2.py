import argparse
import mysql.connector
import re

ap = argparse.ArgumentParser(description='Converts a 3-column table to LATEX to format species based on columns')
ap.add_argument("-co", "--charactersonly", default=False, action='store_true', 
        help="to print only species \t lambda-max")
ap.add_argument("-ho", "--hetonly", default=False, action='store_true', 
        help="to print only heterologously expressed sequences")
args = vars(ap.parse_args())
charactersonly = args["charactersonly"]
hetonly = args["hetonly"]

acc_list = []
duped = 0


if(hetonly == False) :
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9DogsinaTree",
    database="vizphiz"
  )
  
  mycursor = mydb.cursor()

  sql = "select DISTINCT o.genus,o.species,o.accession,l.lamdamax, o.aa from opsins o, lamdamax l WHERE (o.genus = l.genus AND o.species = l.species) AND (o.genefamily like 'Rh1') AND l.celltype like 'rod';"

  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  for x in myresult:
    #Keep all accessions in a list -- don't print 
    if (x[2] in acc_list):
      #print ("\n\n\n****Accession Exists" + x[2] + "\n\n" )
      duped=1
    else: 
      acc_list.append(x[2])
    if (duped==1) :
      duped=0
    else :
  #top prints fasta sequece second prints csv for character data
      if(charactersonly) :
        print(x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "," + str(x[3]))
      else :
        print(">" + x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "\n" + x[4] )

#Heterologous starts here
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9DogsinaTree",
  database="vizphiz"
)
mycursor = mydb.cursor()

sql = "select DISTINCT o.genus,o.species, o.accession,h.lamdamax, o.aa from opsins o, heterologous h WHERE (o.accession = h.accession AND o.genefamily like 'Rh1'); "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
  #Keep all accessions in a list -- don't print 
  if (x[2] in acc_list):
    #print ("\n\n\n****Accession Exists" + x[2] + "\n\n" )
    duped=1
  else: 
    acc_list.append(x[2])


  #First 2 of if statements ignore ancestral (pigment named) or mutated genes
  if (duped==1) :
    duped=0
  #do not print if contains the word "pigment" which is an ancestral sequence
  elif re.match("pigment", x[2]) :
    pass
    #print("PIGMENT " + x[0] + "_" + x[1] + "_" + x[2])
  #do not print mutations
  elif re.match('.+[A-Z]\d.+[A-Z]', x[2]) :
    #print("********************Found " + x[2] )
    pass
  else :
    if(charactersonly) :
      print(x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + ", " + str(x[3]) )
    else :
      print(">" + x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "\n" + x[4] )

