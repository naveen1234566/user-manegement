import psycopg2

def updatetable(user_id, user_address):
    try:
       
        connection = psycopg2.connect(
            database = "usermanegement",
            user = "postgres",
            password = "Network@123",
            host = "localhost",
            port = "5432")
        
        
        cursor = connection.cursor()
        psql_update = """update users set  user_address = %s where user_id = %s"""
        
        # cursor.execute(psql_update,
        #     user_age,
        #     user_id)
        #cursor.execute("INSERT INTO users (user_id, user_age) VALUES (?, ?)", (user_id, user_age) )
        #cursor.execute("UPDATE users SET user_age = ? where user_id = ?", (user_id, user_age))
        
        cursor.execute(psql_update, (user_address,user_id))
        
        connection.commit()
        count = cursor.rowcount
        print(count,"record update successfully")

    except (Exception, psycopg2.Error) as error:
        print("error in update operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("postgresql connection is closed.")

user_id = 3
user_address = 'chennai'
updatetable(user_id, user_address)