import psycopg2
from datetime import datetime as dt
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.ticker import FuncFormatter

conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("chart1.sql", "r").read())
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()

    
    date , sales = zip(*data)

    plt.figure(figsize=(12, 8))
    plt.bar(date, sales)
    plt.title("Total Purchases by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Purchases")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error:", e)