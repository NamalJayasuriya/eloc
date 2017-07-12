#!/usr/bin/python

import MySQLdb
from scipy.io import wavfile
import numpy as np

# Open database connection
db = MySQLdb.connect("localhost","root","root","elocate")

def createDataTable(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS eloc_data")
    sql = """CREATE TABLE IF NOT EXISTS eloc_data (
             location  CHAR(11) NOT NULL,
             time_stamp  INTEGER(11) DEFAULT 0000000000 ,
             channel_1 BLOB NOT NULL ,
             channel_2 BLOB NOT NULL ,
             angle FLOAT )"""
    cursor.execute(sql)

def insertData(db,id,tm,ch1,ch2,ang):
    cursor = db.cursor()
    sql = "INSERT INTO eloc_data(location, time_stamp, channel_1, channel_2, angle) \
    VALUES('%s','%d','%s','%s','%f')"%(id,tm,ch1,ch2,ang)
    try:
        cursor.execute(sql)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0


with open('data', 'rb') as f:
    data1 = f.read()
#print len(data1),data1[:10]

fs, data = wavfile.read("data1.wav")
data=data.astype('float64')
data=data.T
ch1=np.array(data[0]).tostring().encode("hex")
ch2=np.array(data[0]).tostring().encode("hex")

createDataTable(db)
insertData(db,'12345',1499776655,ch1,ch2,87.0)


# disconnect from server
db.close()