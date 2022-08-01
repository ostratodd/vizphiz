import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9DogsinaTree",
  database="vizphiz"
)

#read file for data
file1 = open('heterologous.tsv', 'r')
Lines = file1.readlines()

count=0
for line in Lines:
    columns = line.split("\t")
    print(columns)
    mycursor = mydb.cursor()

    sql = "INSERT INTO heterologous (hetid, genus, species, accession, mutations, lamdamax, error, cellculture, purification, spectrum, sourcetype, refid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (columns[0], columns[1], columns[2], columns[3], columns[4], columns[5], columns[6], columns[7], columns[8], columns[9], columns[10], columns[11])
    print(sql)
    print(val)

#    mycursor.execute(sql, val)

#    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
