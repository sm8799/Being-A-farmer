import MySQLdb
  
# Open database connection 
db = MySQLdb.connect("localhost","shivam","","farmer" ) 
  
cursor = db.cursor() 
  
# Drop table if it already exist using execute() 
  
# Create table as per requirement 
#sql =  "CREATE TABLE EMPLOYEE ( FNAME  CHAR(20) NOT NULL, LNAME  CHAR(20), AGE INT )"
sql = "insert into EMPLOYEE values('shiv', 'marathe', 10)"
print(sql)
cursor.execute(sql) #table created 
db.commit()
# disconnect from server 
db.close() 
