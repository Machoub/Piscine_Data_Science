import psycopg2

conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("remove_duplicates.sql", "r").read())
    print("Duplicates removed successfully")
    conn.commit()
except Exception as e:
    print("Error:", e)
finally:
    cursor.close()
    conn.close()