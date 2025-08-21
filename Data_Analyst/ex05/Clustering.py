import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


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

    nbr_cluster = 5
    data = np.array(data)
    km = KMeans(n_clusters=nbr_cluster).fit(data)
    centroids = km.cluster_centers_

    plt.figure(figsize=(10, 6))
    plt.scatter(data[:, 0], data[:, 1], c=km.predict(data), cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='o', s=200, label='Centroids')

    plt.title("KMeans Clustering of Customer Types")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

except Exception as e:
    print("Error:", e)