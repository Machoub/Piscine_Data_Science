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
    cursor.execute(open("chart.sql", "r").read())
    data = cursor.fetchall()
    print("Data fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()

    nbr_purchase = Counter()
    for x, y in data:
        if y != 'purchase':
            continue
        date_str = dt(x.year, x.month, x.day).strftime("%Y-%b-%d")
        nbr_purchase[date_str] += 1

    parsing = sorted(nbr_purchase.items())
    dates, counts = zip(*parsing)

    plt.figure(figsize=(12, 8))
    plt.plot(dates, counts)
    plt.title("Purchases over time")
    plt.xlabel("Date")
    plt.ylabel("Number of customers")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x / 10)}'))
    plt.xticks(rotation=45)
    tick_positions = [0, len(dates) // 4, 2 * len(dates) // 4, 3 * len(dates) // 4]
    x_labels = ["oct", "nov", "dec", "jan"]
    plt.xticks(tick_positions, x_labels)
    plt.xlim([min(dates), max(dates)])
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error:", e)
