import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Update connection string information
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    )

print("Connection established")

cursor = conn.cursor()
def connexion():
    return cursor

cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL, name VARCHAR(100))")
cursor.execute("INSERT INTO users (name) values ('adlane'), ('johnny')")
cursor.execute("SELECT * from users;")

conn.commit()
cursor.close()
conn.close()
