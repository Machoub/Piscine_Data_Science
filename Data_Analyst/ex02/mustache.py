import psycopg2
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import seaborn as sns

conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("mustache.sql", "r").read())
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()

    dataFrame = pd.DataFrame(data, columns=["user_id", "event_time", "event_type", "price"])

    print("count", dataFrame['event_type'].value_counts().get('purchase', 0))
    print("mean", dataFrame['price'].mean())
    print("std", dataFrame['price'].std())
    print("min", dataFrame['price'].min())
    print("25%", dataFrame['price'].quantile(0.25))
    print("50%", dataFrame['price'].quantile(0.50))
    print("75%", dataFrame['price'].quantile(0.75))
    print("max", dataFrame['price'].max())


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    boxes = ax1.boxplot(dataFrame['price'], vert=False, widths=0.8, notch=True,
            boxprops=dict(facecolor='#81C784', edgecolor='gray'), medianprops=dict(color="gray"),
            flierprops=dict(marker='D', markersize=8, markerfacecolor='gray', markeredgecolor='gray'), patch_artist=True)
    ax1.set_yticks([])
    ax1.set_xlabel('Price')
    ax1.set_title('Boxplot of Price')

    boxprops = dict(facecolor='#81C784', edgecolor='black')
    medianprops = dict(linestyle='-', linewidth=1.5, color='black')
    ax2.boxplot(dataFrame['price'], vert=False, widths=0.5, notch=True,
            boxprops=boxprops, medianprops=medianprops, showfliers=False,
            patch_artist=True)
    ax2.set_yticks([])
    ax2.set_xlabel("Price")
    ax2.set_title("Interquartile range (IQR)")

    plt.tight_layout(); plt.show()

except Exception as e:
    print("Error:", e)