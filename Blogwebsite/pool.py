import pymysql as Mysql

def ConnectionPooling():
    DB=Mysql.connect(host='localhost',port=3306,user='root',password='1234',database='blogwebsite',cursorclass=Mysql.cursors.DictCursor)
    CMD=DB.cursor()
    return DB,CMD