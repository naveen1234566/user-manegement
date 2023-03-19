import psycopg2

conn = psycopg2.connect(
        database = "usermanegement",
        user = "postgres",
        password = "Network@123",
        host = "localhost",
        port = "5432")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

psql = """CREATE TABLE USERS(user_id SERIAL PRIMARY KEY,
                            user_name VARCHAR(250) NOT NULL,
                            user_email VARCHAR(350) NOT NULL,
                            user_password VARCHAR(300) NOT NULL,
                            user_age INT,
                            user_gender VARCHAR(100) NOT NULL,
                            user_address VARCHAR(500) NOT NULL
)"""

cursor.execute(psql)

print("Table created successfully...")
conn.commit()

conn.close()