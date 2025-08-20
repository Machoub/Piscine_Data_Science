import psycopg2
import numpy as np
import matplotlib.pyplot as plt



conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("mustache2.sql", "r").read())
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()
    print("Connection closed")
    averages = [row[1] for row in data]

    plt.figure(figsize=(8, 8))
    plt.boxplot(averages, vert=False, widths=0.7, notch=False, patch_artist=True, boxprops=dict(facecolor="lightblue"),
            flierprops=dict(marker='D', markersize=8, markerfacecolor='gray', markeredgecolor='gray'), medianprops=dict(color='black'),whis=0.2 )
    plt.xlabel("Average Price")
    plt.title("Boxplot of Average Prices")
    plt.yticks([])
    plt.tight_layout()
    plt.xlim(min(averages) - 1, max(averages) + 1)
    plt.xticks(np.arange(min(averages), max(averages)+1, 2))
    plt.show()


except Exception as e:
    print("Error:", e)