import mysql.connector

title=input("Enter DELETE Title:")
try:
	conn = mysql.connector.connect(host='localhost',database='djangoapp',user='root',password='')
	mycursor=conn.cursor()
	mycursor.execute("DELETE FROM todos  WHERE title = '"+title+"'")
	conn.commit()
	print("Delete successfully")
	conn.close() 
except Exception as e:
	print(e)
