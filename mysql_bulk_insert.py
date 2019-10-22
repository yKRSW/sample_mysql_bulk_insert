# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of MySQL bulk insert
"""

import pymysql
import datetime

print("Connect to DB")
conn = pymysql.connect(user="root", password="", host="localhost", database="test")


# Bulk Insert
def insert_data_bulk(values):
    print("Insert bulk data")
    insert_sql = "INSERT INTO test.hoge (name, value, text) values (%s,%s,%s)"

    cur = conn.cursor()
    cur.executemany(insert_sql, values)

# Insert one by one
def insert_data(values):
    insert_sql = "INSERT INTO test.hoge (name, value, text) values (%s,%s,%s)"

    cur = conn.cursor()
    for value in values:
        cur.execute(insert_sql, value)


def main():
    # Generate data
    values = []
    print("Generate data")
    for i in range(100000):
        name = "name_{}".format(i)
        value = i
        text = "text_{}".format(i)
        values.append([name,value,text])
    print("Length of data: {}".format(len(values)))
    print()

    # Insert one by one
    print("Insert data")
    start_time = datetime.datetime.now()
    print("Start:" + str(start_time))
    insert_data(values)
    end_time = datetime.datetime.now()
    print("End:" + str(end_time))
    diff_time = end_time - start_time
    print("Diff:" + str(diff_time))
    print()

    # Bulk Insert
    print("Insert data")
    start_time = datetime.datetime.now()
    print("Start:" + str(start_time))
    insert_data_bulk(values)
    end_time = datetime.datetime.now()
    print("End:" + str(end_time))
    diff_time = end_time - start_time
    print("Diff:" + str(diff_time))
    print()


if __name__ == "__main__":
    main()