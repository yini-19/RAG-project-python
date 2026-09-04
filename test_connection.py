from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
database_url = os.getenv("DATABASE_URL")
print("DATABASE_URL is:", repr(database_url))


if not database_url:
    raise ValueError("DATABASE_URL not found - check your .env file")

try:
    connection=psycopg2.connect()
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    result=cursor.fetchone()
    print("connection successful")
    print("postgres version:", result[0])
    
    cursor.close()
    connection.close()

except Exception as e:
    print("Connection failed", e)