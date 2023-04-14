from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="Kirill",
        password="123456789@kirill",
    ) as connection:
        print(connection);
        print("Success connect admin");
        create_db_query = "CREATE DATABASE users";
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
except Error as e:
    print(e)
