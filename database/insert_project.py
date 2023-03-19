import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                password="Network@123",
                                host="127.0.0.1",
                                port="5432",
                                database="usermanegement")

    cursor = connection.cursor()

    psql_insert_query = """INSERT INTO users(user_id,user_name,user_email,user_password,user_age,user_gender,user_address)
    VALUES(%s,%s,%s,%s,%s,%s,%s)"""

    record_insert = [(6, 'Surya', 'surya@gmail.com',  'surya&04', 25, 'Male', 'Goa'),]

    for i in record_insert:
        cursor.execute(psql_insert_query, i)

        connection.commit()
        count = cursor.rowcount
    print(count, "Record insert successfully \ into users table")


except (Exception,psycopg2.Error) as error:
    print("Failed to insert record into users table", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")