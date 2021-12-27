import mysql.connector

cnx = mysql.connector.connect(user='root',  password="9DogsinaTree", database='vizphiz')
cursor = cnx.cursor()

#Example
#query = ("SELECT first_name, last_name, hire_date FROM employees "
#         "WHERE hire_date BETWEEN %s AND %s")
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)
#cursor.execute(query, (hire_start, hire_end))

query = ("select o.genus,o.species,l.lamdamax from opsins o, lamdamax l WHERE (o.genus = l.genus AND o.species = l.species) AND (o.genefamily like 'Rh1') AND l.celltype like 'rod';")
cursor.execute(query)

#query = ("SELECT genus, species, lamdamax from lamdamax WHERE celltype like 'rod';")
#cursor.execute(query)


print(cursor)
for (o.genus, o.species, l.lamdamax) in cursor:
   print("{}_{}_{}".format(o.genus, o.species, l.lamdamax))

#  print("{}, {} was hired on {:%d %b %Y}".format(
#    last_name, first_name, hire_date))

cursor.close()
cnx.close()
