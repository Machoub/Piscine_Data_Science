import psycopg2
import matplotlib.pyplot as plt

conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("chart.sql", "r").read())
    print("Data fused successfully")
    data = cursor.fetchall()
    print("Fetched data:", data)
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
