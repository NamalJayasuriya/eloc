#import MySQLdb


# prepare a cursor object using cursor() method
def dropTable(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS eloc_data")


def createDataTable(db):
    cursor = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS eloc_data (
             location  INTEGER(11)  NOT NULL,
             time_stamp INTEGER(11) DEFAULT 0000000000 ,
             data_file VARCHAR(45) NOT NULL ,
             angle FLOAT )"""
    cursor.execute(sql)


def insertData(db,id,tm,df,ang):
    cursor = db.cursor()
    sql = "INSERT INTO eloc_data(location, time_stamp, data_file, angle) VALUES('%d','%d','%s','%f')"%(id,tm,df,ang)
    try:
        cursor.execute(sql)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0

def getColomn(db,col):
    cursor = db.cursor()
    sql = "SELECT "+col+" FROM eloc_data group by "+col
    loc=[]
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            loc.append(row[0])
        return loc

    except:
        print "Error: unable to fecth data"
        return 0

def getColomnWhere(db,col,loc):
    cursor = db.cursor()
    sql = "SELECT "+col+" FROM eloc_data where location="+loc
    loc=[]
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            loc.append(row[0])
        return loc

    except:
        print "Error: unable to fecth data"
        return 0

def getData(db,loc,tim):
    cursor = db.cursor()
    sql = "SELECT data_file, angle FROM eloc_data where location="+loc+" and time_stamp="+tim
    dict={}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        i=0
        for row in results:
            dt={}
            dt["data_file"]=row[0]
            dt["angle"] = row[1]
            dict[i]=dt
            i=i+1
        return dict

    except:
        print "Error: unable to fecth data"
        return 0