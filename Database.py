#Database
import os
import csv
import pandas as pd
import mysql.connector
def MakeDBandTbl():
	os.system("cls")	
	global username
	global pswd
	username,pswd=input("Enter username(By Default \'root\''):"),input("Enter password for mySQL database:")
	entry=input("Is the database and the table already created?(Y/N)\n")
	if(entry=='N'):	
		mydb=mysql.connector.connect(host="localhost", user=username, password=pswd)
		myc=mydb.cursor()
		myc.execute("CREATE DATABASE JoC_logs")
		mydb.commit()
		mydb=mysql.connector.connect(host="localhost", user=username, password=pswd,database="joc_logs")
		myc=mydb.cursor()
		myc.execute("USE joc_logs")
		myc.execute("CREATE TABLE Records(USER VARCHAR(21) NOT NULL, METHOD VARCHAR(21) NOT NULL, ENCRYPTION VARCHAR(300) NOT NULL, TIMESTAMPED VARCHAR(30) NOT NULL)")
		mydb.commit()
		mydb.close()

	else:
		print("Press enter to continue.")



def AddRecord(user,method,encryption,time):
	
	mydb=mysql.connector.connect(host="localhost", user=username, password=pswd, database="joc_logs")
	myc=mydb.cursor()
	myc.execute("USE joc_logs")
	myc.execute("INSERT INTO Records VALUES (\""+user+"\",\""+method+"\",\""+encryption+"\",\""+time+"\")")
	mydb.commit()
	mydb.close()
	with open("JoC_logs.csv" ,"a" , newline='') as file:
		writer = csv.writer(file)
		writer.writerow([user,method,encryption,time])
	file.close()
	#print("Done")


def Read():                                                         
	print("8 8888         ,o888888o.         ,o888888o.      d888888o.   ")
	print("8 8888      . 8888     `88.      8888     `88.  .`8888:' `88. ")
	print("8 8888     ,8 8888       `8b  ,8 8888       `8. 8.`8888.   Y8 ")
	print("8 8888     88 8888        `8b 88 8888           `8.`8888.     ")
	print("8 8888     88 8888         88 88 8888            `8.`8888.    ")
	print("8 8888     88 8888         88 88 8888             `8.`8888.   ")
	print("8 8888     88 8888        ,8P 88 8888   8888888    `8.`8888.  ")
	print("8 8888     `8 8888       ,8P  `8 8888       .8'8b   `8.`8888. ")
	print("8 8888      ` 8888     ,88'      8888     ,88' `8b.  ;8.`8888 ")
	print("8 888888888888 `8888888P'         `8888888P'    `Y8888P ,88P' ")
	print("\n\nLogs:\n")
	data=pd.read_csv("JoC_logs.csv")
	print(data)
	a=input()
