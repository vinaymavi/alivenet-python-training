import mysql.connector

title=input("Enter Title:")
dec=input("ENter Dec:")
try:
	conn = mysql.connector.connect(host='localhost',database='djangoapp',user='root',password='')
	mycursor=conn.cursor()
	mycursor.execute("UPDATE todos SET descs = '"+dec+"' WHERE title = '"+title+"'")
	conn.commit()
	print("update successfully")
	conn.close() 
except Exception as e:
	print(e)
