import mysql.connector as msc

connection = msc.connect(
  host="localhost",
  user="root",
  passwd="deepa",
  database="ecra_students"
)
cursor = connection.cursor()

#cursor.execute ("DROP TABLE IF EXISTS ")
cursor.execute("""DROP TABLE employee;""")
query = """
CREATE TABLE employee ( 
SAP_ID INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(20), 
Address VARCHAR(30), 
birth_date DATE);"""

cursor.execute(query)
print("Record created successfully")

staff_data = [ ("Ailliam", "Shakespeare", "address1", "1961-10-25"),
               ("Hrank", "Schiller", "address2", "1955-08-17"),
               ("Mane", "Wall", "address3", "1989-03-14"),
               ]
               
for staff, p in enumerate(staff_data):
    format_str = """INSERT INTO employee (SAP_ID, fname, lname, address, birth_date)
    VALUES ({SAP_ID}, '{first}', '{last}', '{address}', '{birthdate}');"""

    query = format_str.format(SAP_ID=staff, first=p[0], last=p[1], \
                              address=p[2], birthdate = p[3])
    cursor.execute(query)

print("data inserted successfully")


cursor.execute("SELECT * FROM employee")
result= cursor.fetchall()
print(type(result))
print('''Result of "SELECT * FROM employee":''')
for r in result:
    print(r)

    
cursor.execute("SELECT fname FROM employee where fname LIKE 'H%'") 
result = cursor.fetchall()
print("\nResult of students whose name starts with H is\n", result)
print("\n")


cursor.execute("SELECT * FROM employee ORDER BY fname DESC")
result = cursor.fetchall()
print("\n")
for r in result:
    print(r)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()




