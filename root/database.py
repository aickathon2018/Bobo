import sqlite3, sys
import numpy as np

if len(sys.argv) < 2:
    print("Usage: python database.py [database_name].db")
    sys.exit()
database = sys.argv[1]

db = sqlite3.connect(database)

cursor = db.cursor()

try:
    tablename = "User"
    print('\n ------------- drop table <{tn}> if it exists'.format(tn=tablename))
    cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=tablename))

    print("creating table: {tn}".format(tn=tablename))
    create_table = '''CREATE TABLE {tn} (
                user_id     integer     not null    default 0 PRIMARY KEY AUTOINCREMENT,
                username    varchar(32) not null    default '',
                password    varchar(64) not null    default '',
                age         integer     not null    default 1,
                gender      varchar(1)  not null    default 'u'
                );'''.format(tn=tablename)
    print('\n', create_table)
    cursor.execute(create_table)
except:
    print("Error occured during table User creation.")
else:
    print("Table {tn} created successfully!".format(tn=tablename))
