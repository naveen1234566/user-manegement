import psycopg2

try:
    connection = psycopg2.connect( 
        database = "usermanegement",
        user = "postgres",
        password = "Network@123",
        host = "localhost",
        port = "5432")
    
    cursor = connection.cursor()
    psql_select_query = "select * from users"
    
    cursor.execute(psql_select_query)
    print("selecting row from users table using cursor.fetchall")
    users_records = cursor.fetchall()
   
    print("print each row and columns values:")
    for row in users_records:
        print("user_id=",row[0])
        print("user_name=",row[1])
        print("user_email=",row[2])
        print("user_passwor=",row[3])
        print("user_age=",row[4])
        print("user_gender=",row[5])
        print("user_address=",row[6],"\n")

except (Exception, psycopg2.Error) as error:
    print("error while fetching data from psql", error)
    
finally:
    if connection:
        cursor.close()
        connection.close()
        print("postgresql connection is closed.")
