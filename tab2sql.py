import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9DogsinaTree",
  database="vizphiz"
)

mycursor = mydb.cursor()

sql = "INSERT INTO opsins (opsinid, dna) VALUES (%s, %s)"
val = (100, "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
