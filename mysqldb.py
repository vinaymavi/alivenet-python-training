from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
try:
    emp_no=input("Enter Employee Code:")
    salary=input("Enter Employee Salalry:")
      #mysql connection
    if(emp_no!='' and salary!=''):
      connect_db = mysql.connector.connect(user='root', database='test')
      query = connect_db.cursor()
      tomorrow = datetime.now().date() + timedelta(days=1)
      #mysql query
      query.execute("INSERT INTO salaries "
      "(emp_no, salary, from_date, to_date) "
      "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)", {'emp_no': emp_no,'salary': salary,'from_date': tomorrow, 'to_date': tomorrow})
      connect_db.commit()
      query.close()   
      connect_db.close()
      #end 
      print("Salary save successfully")
    else:
        print("Please enter vlaues")   
except exception as error:
                          print("Error"+error)
     
  
      

