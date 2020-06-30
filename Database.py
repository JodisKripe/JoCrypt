#Database
import os
import mysql.connector
def MakeDBandTbl():
	os.system("cls")	
	global username
	global pswd
	username,pswd=input("Enter username(By Default \'root\'')."),input("Enter password for mySQL database.")
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
	#print("Done")
