import psycopg2
import numpy as np
import pandas as pd
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

    df = pd.DataFrame(data, columns=['user_id', 'order_count', 'total_spent'])
    print("DataFrame created successfully")
    
    std_scaler = StandardScaler()
    data_for_clustering = std_scaler.fit_transform(df[['order_count', 'total_spent']])
    print("Data standardized successfully")

    num_clusters = 4
    km = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = km.fit_predict(data_for_clustering)
    print("KMeans model fitted successfully")

    df['cluster'] = clusters
    centroids = km.cluster_centers_
    centroids_original = std_scaler.inverse_transform(centroids)

    plt.figure(figsize=(10, 6))
    for cluster in df["cluster"].unique():
        cluster_data = df[df["cluster"] == cluster]
        plt.scatter(
            cluster_data["order_count"],
            cluster_data["total_spent"],
            label=f"Cluster {cluster}"
            )
    plt.scatter(
        centroids_original[:, 0],
        centroids_original[:, 1],
        color="black",
        marker="o",
        s=50,
        label="Centroids"
        )
    plt.title("Customer Clusters: Total Spent vs. Order Count")
    plt.xlabel("Order Count")
    plt.ylabel("Total Spent (Altairian Dollars)")
    plt.legend()
    plt.grid()
    plt.show()

    counts_per_cluster = df.groupby("cluster").size().sort_values(ascending=False)
    plt.figure(figsize=(8, 6))
    counts_per_cluster.plot(kind="barh")
    plt.title("Nombre de clients par cluster")
    plt.ylabel("Cluster")
    plt.xlabel("Nombre de clients")
    plt.yticks(rotation=0)
    plt.gca().invert_yaxis()  # optionnel : mettre le plus grand en haut
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error:", e)