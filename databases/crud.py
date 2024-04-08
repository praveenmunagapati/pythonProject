# # Python implementation to create a Database in MySQL
# import mysql.connector
#
# # connecting to the mysql server
# db = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd=""
# )
#
# # cursor object c
# c = db.cursor()
#
# # executing the create database statement
# c.execute("CREATE DATABASE employee_db")
#
# # fetching all the databases
# c.execute("SHOW DATABASES")
#
# # printing all the databases
# for i in c:
# 	print(i)
# c = db.cursor()
#
# # finally closing the database connection
# db.close()


# Python implementation to create a table in MySQL
# import mysql.connector
#
# # connecting to the mysql server
#
# db = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd="",
# 	database="employee_db"
# )
#
# # cursor object c
# c = db.cursor()
#
# # create statement for tblemployee
# employeetbl_create = """CREATE TABLE `employee_db`.`tblemployee` (
# `empid` INT NOT NULL AUTO_INCREMENT,
# `empname` VARCHAR(45) NULL,
# `department` VARCHAR(45) NULL,
# `salary` INT NULL,
# PRIMARY KEY (`empid`))"""
#
# c.execute(employeetbl_create)
#
# c = db.cursor()
#
# # fetch tblemployee details in the database
# c.execute("desc tblemployee")
#
# # print the table details
# for i in c:
# 	print(i)
#
#
# # finally closing the database connection
# db.close()

# Python implementation to insert data into a table in MySQL
# import mysql.connector
#
# # connecting to the mysql server
#
# db = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd="",
# 	database="employee_db"
# )
#
# # cursor object c
# c = db.cursor()
#
# # insert statement for tblemployee
# # this statement will enable us to insert multiple rows at once.
# employeetbl_insert = """INSERT INTO tblemployee (
# empname,
# department,
# salary)
# VALUES (%s, %s, %s)"""
#
# # we save all the row data to be inserted in a data variable
# data = [("Vani", "HR", "100000"),
# 		("Krish", "Accounts", "60000"),
# 		("Aishwarya", "Sales", "25000"),
# 		("Govind", "Marketing", "40000")]
#
# # execute the insert commands for all rows and commit to the database
# c.executemany(employeetbl_insert, data)
# db.commit()
#
# # finally closing the database connection
# db.close()

# # Python implementation to fetch data from a table in MySQL
# import mysql.connector
#
# # connecting to the mysql server
#
# db = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd="",
# 	database="employee_db"
# )
#
# # cursor object c
# c = db.cursor()
#
# # select statement for tblemployee which returns all columns
# employeetbl_select = """SELECT * FROM tblemployee"""
#
# # execute the select query to fetch all rows
# c.execute(employeetbl_select)
#
# # fetch all the data returned by the database
# employee_data = c.fetchall()
#
# # print all the data returned by the database
# for e in employee_data:
# 	print(e)
#
# # finally closing the database connection
# db.close()
# Python implementation to update data of a table in MySQL
# import mysql.connector
#
# # connecting to the mysql server
#
# db = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd="",
# 	database="employee_db"
# )
#
# # cursor object c
# c = db.cursor()

# update statement for tblemployee
# which modifies the salary of Vani
# employeetbl_update = "UPDATE tblemployee SET salary = 115000 WHERE empid = 1"
#
# # execute the update query to modify
# # the salary of employee with
# # employee id = 1 and commit to the database
# c.execute(employeetbl_update)
# db.commit()
#
# # finally closing the database connection
# db.close()

import mysql.connector

# connecting to the mysql server

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="employee_db"
)
print("beore commit")
# cursor object c
c = db.cursor()
employeetbl_select = """SELECT * FROM tblemployee"""

# execute the select query to fetch all rows
c.execute(employeetbl_select)

# fetch all the data returned by the database
employee_data = c.fetchall()

# print all the data returned by the database
for e in employee_data:
	print(e)

# delete statement for tblemployee
# which deletes employee Aishwarya having empid 3
employeetbl_delete = "DELETE FROM tblemployee WHERE empid=3"

# execute the delete statement and commit to the database
c.execute(employeetbl_delete)
db.commit()
print("after commit")
employeetbl_select = """SELECT * FROM tblemployee"""

# execute the select query to fetch all rows
c.execute(employeetbl_select)

# fetch all the data returned by the database
employee_data = c.fetchall()

# print all the data returned by the database
for e in employee_data:
	print(e)

# finally closing the database connection
db.close()
