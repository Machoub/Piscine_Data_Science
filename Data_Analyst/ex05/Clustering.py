import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    with open("Clustering.sql", "r") as file:
        sql_script = file.read()
    print("SQL scripts loaded successfully")
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(sql_script)
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()
    print("Connection closed")

    test = [row for row in data]
    print("Test data prepared", test)

except Exception as e:
    print("Error:", e)