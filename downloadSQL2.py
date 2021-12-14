import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9DogsinaTree",
  database="vizphiz"
)

mycursor = mydb.cursor()

sql = "select o.genus,o.species,l.lamdamax, o.aa from opsins o, lamdamax l WHERE (o.genus = l.genus AND o.species = l.species) AND (o.genefamily like 'Rh1') AND l.celltype like 'rod';"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(">" + x[0] + "_" + x[1] + "_" + str(x[2]) + "\n" + x[3] )



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9DogsinaTree",
  database="vizphiz"
)

mycursor = mydb.cursor()

sql = "select DISTINCT o.genus,o.species, h.lamdamax, o.aa from opsins o, heterologous h WHERE (o.accession = h.accession AND o.genefamily like 'Rh1'); "


mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(">" + x[0] + "_" + x[1] + "_" + str(x[2]) + "\n" + x[3] )
