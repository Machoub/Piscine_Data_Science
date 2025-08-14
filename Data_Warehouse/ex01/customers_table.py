import psycopg2

conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("customers_table.sql", "r").read())
    print("Table created successfully")
    conn.commit()
except Exception as e:
    print("Error:", e)
finally:
    cursor.close()
    conn.close()
