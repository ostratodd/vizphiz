import mysql.connector
import re

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

acc_list = []
duped = 0

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
#    print(">" + x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "\n" + x[4] )
    print(x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "," + str(x[3]))



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
  elif re.match("pigment", x[2]) :
    pass
    #print("PIGMENT " + x[0] + "_" + x[1] + "_" + x[2])
  elif re.match('.+[A-Z]\d.+[A-Z]', x[2]) :
    #print("********************Found " + x[2] )
    pass
  else :
#top prints fasta sequece second prints csv for character data
#    print(">" + x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + "\n" + x[4] )
    print(x[0] + "_" + x[1] + "_" + x[2] + "_" + str(x[3]) + ", " + str(x[3]) )
