import sqlite3


db_connection = sqlite3.connect('FastFasting.db')
cursor = db_connection.cursor()
cursor.execute('''select * from fasting''')
contents = cursor.fetchall()
for entry in contents:
    print(entry)
print('---')
sql = 'SELECT * FROM fasting WHERE Id = (SELECT MAX(Id) FROM fasting)'
cursor.execute(sql)
print(cursor.fetchall())

