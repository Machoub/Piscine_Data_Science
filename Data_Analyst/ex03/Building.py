import psycopg2
import numpy as np
import matplotlib.pyplot as plt



conn_string = "host='localhost' dbname='piscineds' user='machouba' password='mysecretpassword' port='5432'"

try:
    with open("Building.sql", "r") as file:
        sql_script = file.read()
    with open("Building1.sql", "r") as file:
        sql_script1 = file.read()
    print("SQL scripts loaded successfully")
    conn = psycopg2.connect(conn_string)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute(sql_script)
    data_frequency = cursor.fetchall()
    print("Data_frequency fetched successfully")
    cursor.execute(sql_script1)
    data_monetary = cursor.fetchall()
    print("Data_monetary fetched successfully")
    conn.commit()
    cursor.close()
    conn.close()
    print("Connection closed")

    freq = [row[1] for row in data_frequency if row[1] <= 40]
    mony = [row[1] for row in data_monetary]

    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    ax[0].grid(True,zorder=-1)
    ax[0].hist(freq, bins=5, edgecolor='k')
    ax[0].set_xlabel("Frequency")
    ax[0].set_ylabel("Customers")
    ax[0].set_xticks(range(0, 39, 10))
    ax[0].set_ylim(0, 60000)

    ax[1].grid(True,zorder=-1)
    ax[1].hist(mony, bins=5, edgecolor='k')
    ax[1].set_xlabel("Monetary value in A")
    ax[1].set_ylabel("Customers")

    for a in ax:
        a.yaxis.grid(True, linestyle='-', alpha=0.7)
        a.set_axisbelow(True)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error:", e)