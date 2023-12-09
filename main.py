import psycopg2

DATABASE = 'test_db'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '55555'

connection = psycopg2.connect(
    database=DATABASE,
    user=USER,
    host=HOST,
    password=PASSWORD,
    port=PORT,
)

cursor = connection.cursor()

# add data
cursor.execute("INSERT INTO instructors(name) VALUES('Ban');")
cursor.execute("INSERT INTO instructors(name) VALUES('Marta');")
connection.commit()
cursor.close()
connection.close()


