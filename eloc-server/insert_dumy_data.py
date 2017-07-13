#!/usr/bin/python

import MySQLdb
from dbHandler import insertData, createDataTable,dropTable
from os import listdir

# Open database connection
db = MySQLdb.connect("localhost","root","root","elocate")



path='./eloc_data/123456789/'
files = listdir(path)
print files
dropTable(db)
createDataTable(db)
id=123456789
for i in files:
    print insertData(db,id,int(i[:-4])+0,path+str(i),87.0)

db.close()