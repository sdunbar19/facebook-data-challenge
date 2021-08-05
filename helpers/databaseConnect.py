import mysql.connector

def get_conn_cursor(db):
    try:
        conn = mysql.connector.connect(user='root', password='password', database=db)
        return conn, conn.cursor()
    except mysql.connector.Error as err:
        print(err)

def makeQuery(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result