import psycopg2
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
from collections import defaultdict




conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(open("chart2.sql", "r").read())
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()

    monthly_sales = defaultdict(float)
    unique_users = defaultdict(set)

    for user_id, event_time, event_type, price in data:
        event_month = event_time.strftime("%Y-%m-%d")
        monthly_sales[event_month] += price
        unique_users[event_month].add(user_id)

    date = sorted(monthly_sales.keys())
    average_spend_per_customer = [monthly_sales[date] * 0.8 / len(unique_users[date]) if unique_users[date] else 0 for date in date]
    

    plt.figure(figsize=(12, 8))
    plt.plot(date, average_spend_per_customer, color='blue', alpha=0.3)
    plt.fill_between(date, average_spend_per_customer, color='blue', alpha=0.3)
    plt.ylabel("Average Spend/Customer in A")
    tick_positions = [0, len(date) // 4, 2 * len(date) // 4, 3 * len(date) // 4]
    tick_labels = ["Oct", "Nov", "Dec", "Jan"]
    plt.xticks(tick_positions, tick_labels)
    plt.xticks(rotation=45)
    plt.yticks(np.arange(0, max(average_spend_per_customer), 5))
    plt.ylim(0)
    plt.xlim(date[0], date[-1])
    plt.show()

except Exception as e:
    print("Error:", e)