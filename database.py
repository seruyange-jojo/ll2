import mysql.connector
 
try:
    conn = mysql.connector.connect(
                                    database='application',
                                    host='localhost',
                                    user='cbuser',
                                    password='cbpass'
                                )
    print('Connected')
except:
    print('Cannot connect to the server')
    print('Error code: %s' % e.errno )
    print('Error Message: %s' % e.msg)
    print('Error SQLSTATE: %s' % e.sqlstate)
else:
    # conn.close()
    # print('Disconnected')
    pass

cursor = conn.cursor()
cursor.execute("UPDATE profilee set cats = cats+4 where namee = 'Sybil'")
cursor.execute("INSERT INTO profilee (namee, color, foods, cats) values ('Richard', 'green', 'curry', 54)")
print('Number of rows updated: %d ' %cursor.rowcount)
cursor.close()
conn.commit()

# printing multiple rows after using a select statement
cursor = conn.cursor()
cursor.execute('select id, namee , cats from profilee')
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print('id: %s, namee: %s, cats: %s' % (row[0], row[1], row[2]))
print('Number of rows returned is: %d' % cursor.rowcount)
cursor.close()

# Another alternative
cursor = conn.cursor()
cursor.execute('select id, namee, cats from profilee')
for (id, namee, cats) in cursor:
    print('id: %s, namee: %s, cats: %s' % (id, namee, cats))
print('Number of rows returned is: %d' % cursor.rowcount)
cursor.close()

# Another alternative
cursor = conn.cursor()
cursor.execute('select id, namee, cats from profilee')
rows = cursor.fetchall()
for row in rows:
    print('id: %s, namee: %s, cats: %s' % (row[0], row[1], row[2]))
print("Number of rows returned is : %d " % cursor.rowcount )
cursor.close()


# Quoting function in python for dealing with null , quotes and other data types that might be utilised in sql injection attacks
str = ''
if len(values) > 0:
    str = "?"
for i in range(1, len(values)):
    str += ',?'

# Using placeholder values inside the value clause ---Method 2
cursor = conn.cursor()
cursor.execute(
    '''
    INSERT INTO PROFILE (name , birth, color, food, cats) values (%s, %s, %s, %s, %s)
    ''', ("De'Mont", '2003-12-13', None, 'eggroll', 43))
cursor.close()
conn.commit()


# Testing for null values
cursor = conn.cursor()
cursor.execute('select name, birth, food from profile')
for row in cursor:
    row = list(row)
    for i, value in enumerate(row):
        if value is None:
            row[i] = "NULL"
        print('Name: %s, food: %s, cats: %s' (row[0], row[1], row[2]) )
    cursor.colse()


conn.close()
print('Disconnected')