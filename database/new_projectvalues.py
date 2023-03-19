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

    record_insert = [(1, 'Naveen', 'naveen@gmail.com', 'Naveen@123', 25, 'Male',  'Chennai'),
                    (2, 'Vinoth', 'vinoth@gmail.com', 'Vinoth@321', 28, 'Male','Chennai'),
                    (3, 'Athiyan', 'athi@gmail.com',  'Athi@412', 20, 'Male', 'Mumbai'),
                    (4, 'Kavitha', 'kavi12@gmail.com',  'Kavith@21', 21, 'Female', 'Bangalore'),
                    (5, 'Jessi', 'jessi22@gmail.com',  'Jessi$22', 23, 'Female', 'Bangalore'),
                    (6, 'Surya', 'surya@gmail.com',  'surya&04', 25, 'Male', 'Goa'),
                    (7, 'Priya', 'priya95@gmail.com', 'priya@95', 24, 'Female', 'Goa')]

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