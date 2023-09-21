import mysql.connector

def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="kshitiz"
    )
    cursor = conn.cursor()
    return conn, cursor

def close_database_connection(conn, cursor):
    cursor.close()
    conn.close()
                                                                                                                                                                                            