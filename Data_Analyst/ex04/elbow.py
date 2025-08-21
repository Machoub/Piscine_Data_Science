import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    with open("elbow.sql", "r") as file:
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
    
    ks = []
    for k in range(1, 11):
        KM = KMeans(n_clusters=k, n_init=10, random_state=42).fit(data)
        ks.append(KM.inertia_)


    plt.plot(range(1, 11), ks, marker='o')
    plt.xlabel("Number of clusters")
    plt.title("The Elbow Method")
    plt.show()

except Exception as e:
    print("Error:", e)