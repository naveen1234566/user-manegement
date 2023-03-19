import psycopg2

def deletedata(user_id):

    try:
        connection = psycopg2.connect(
            database = "usermanegement",
            user = "postgres",
            password = "Network@123",
            host = "localhost",
            port = "5432")

        cursor = connection.cursor()

        psql_delte_query = """Delete from users  where user_id = %s"""

        cursor.execute(psql_delte_query, (user_id))
        connection.commit()
        count = cursor.rowcount
        print(count,"record delete successfully")

    except (Exception,psycopg2.Error) as error:
        print("error in delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("postgresql connection is closed")

user_id = '6'
deletedata(user_id)
