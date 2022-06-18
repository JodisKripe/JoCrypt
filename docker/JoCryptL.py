'''

Linux version

'''
import os
#import msvcrt
import subprocess
#import ctypes
#from ctypes import wintypes
import itertools
import hashlib
#from stegano import lsb
import math
'''
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)
'''
'''
def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
'''
##############################################################################################################################################################
def BoxCipher():
	import math
	message = input("~$-").strip()
	message = message.replace(" ", "")
	l = len(message)
	sl = math.sqrt(l)
	r = math.floor(sl)
	c = int(sl)

	ldscr()   

	decry=[]
	fin=''
	decry=message.split(' ')
	for i in range(0,len(decry)):
		fin=fin+str(decry[i])
		i=i+1

	dole=list(fin)


	box_rows=[dole[i:i+r] for i in range(0, len(dole), r)]

	print("")

	for _ in range(0,len(box_rows)):
		print(box_rows[_])


	for i in range(0, c):
		print(message[i : l : r], end = " ")



	bye=input()

##################################################################################################################################################################
def BoxCipherDecryption(text):
	message=text #input("Please enter message to be Decrypted:")
	message=message.split(" ")
	tex=''
	for i in range(len(message)):
		tex+=message[i]

	l=len(tex)
	sl=math.sqrt(l)
	r=math.floor(sl)
	c=int(sl)
	fin=list(tex)
	boxr=[fin[i:i+c] for i in range(0,len(fin),c)]
	#for i in range(0, c):
	#	print(tex[i : l : c+1], end = " ")
	jj=''
	x=0
	for i in range(c):
		for j in range(l%r):
			jj+=tex[x]
			x+=c+1
		for j in range(r-l%r):
			jj+=tex[x]
			x+=c
		x=i+1
	last=''
	for i in range(l%r):
		last+=message[i][-1]
	ldscr()
	#print("The encrypted message is:\n"+str(jj+last))
	return str(jj+last)


##################################################################################################################################################################

def Substitution(text):
	mess=text
	mess=mess.lower()

	replace={'a':"$",'b':"v",'c':"@",'d':"g",'e':"^",'f':"|",'g':"\\",'h':"5",'i':"2",'j':"u",'k':"8",
			'l':"w",'m':"*",'n':"7",'o':"m",'p':"q",
			'q':"p",'r':"%",'s':"(",'t':")",'u':"z",'v':"3",'w':"!",'x':"_",'y':"=",'z':":",'1':"a",'2':"n",'3':"x",'4':"o",
			'5':"~",'6':"`",'7':"/",'8':"d",'9':"i",'0':"+",' ':"6",',':"r",'.':"c"}
	jj=list(mess)

	encryption=''

	for i in range(0,len(jj)):
		encryption=encryption + str(replace[jj[i]])

	ldscr()  
	return encryption

#####################################################################################################################################################################

def ReverseString(text):	
	message= text #input("This Cipher does exactly what it says\n\n~$-")
	arr=list(message)

	encryption=''

	for i in range(1,(len(arr)+1)):
		encryption = encryption + str(arr[-i])

	ldscr()  
	return encryption
##################################################################################################################################################################
def CaesarDecrypt(text,key):
	text = text #input("enter string: ")
	s = key # int(input("enter shift number: "))
	cipher = ''
	for char in text: 
		if char == ' ':
			cipher = cipher + char
		elif  char.isupper():
			cipher = cipher + chr((ord(char) - s - 65) % 26 + 65)
		else:
			cipher = cipher + chr((ord(char) - s - 97) % 26 + 97)
	ldscr()
	
	return cipher
	
 

##################################################################################################################################################################
def CaesarEncrypt(text,key):
	string= text #input("Enter String to be encrypted: ")
	shift=key #int(input("Enter Shift/Key: "))

	cipher = ''
	for char in string: 
		if char == ' ':
			cipher = cipher + char
		elif  char.isupper():
			cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
		else:
			cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
	ldscr()

	return cipher
	#cip=input()


##################################################################################################################################################################
def encryptRailFence(text,key):                                                                              
	#text=input("Input Text to be encrypted:")
	#key=int(input("Enter Key:"))
	#text=text

	rail = [['\n' for i in range(len(text))] 
					for j in range(key)] 
      
	dir_down = False
	row, col = 0, 0
      
	for i in range(len(text)): 

		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
          
 
		rail[row][col] = text[i] 
		col += 1
          

		if dir_down: 
			row += 1
		else: 
			row -= 1

	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	ldscr()
	encry="" . join(result)
	return encry 
	#cham=input()      
 
##################################################################################################################################################################
def decryptRailFence(text,key): 
	#cipher=input("Input Cipher to be decrypted:")
	#key=int(input("Enter Key: "))  
	cipher=text
	key=key

	rail = [['\n' for i in range(len(cipher))]  
					for j in range(key)] 

	dir_down = None
	row, col = 0, 0
      

	for i in range(len(cipher)): 
		if row == 0: 
			dir_down = True
		if row == key - 1: 
			dir_down = False
          

		rail[row][col] = '*'
		col += 1
          

		if dir_down: 
			row += 1
		else: 
			row -= 1
              

	index = 0
	for i in range(key): 
		for j in range(len(cipher)): 
			if ((rail[i][j] == '*') and
				(index < len(cipher))): 
				rail[i][j] = cipher[index] 
				index += 1
          

	result = [] 
	row, col = 0, 0
	for i in range(len(cipher)): 
          
		if row == 0: 
			dir_down = True
		if row == key-1: 
			dir_down = False
              

		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
              

		if dir_down: 
			row += 1
		else: 
			row -= 1
	ldscr()
	mess="".join(result)
	return(mess)
	#lamas=input() 
##################################################################################################################################################################
def ReverseSubstitution(text):
		#encry=input("You can decode the code encrypted by the SubstitutionCipher\n\n~$-")
		encry=text
		jj=list(encry)
		replace={'$':"a",'v':"b",'@':"c",'g':"d",'^':"e",'|':"f",'\\':"g",'5':"h",'2':"i",'u':"j",'8':"k",
				'w':"l",'*':"m",'7':"n",'m':"o",'q':"p",
				'p':"q",'%':"r",'(':"s",')':"t",'z':"u",'3':"v",'!':"w",'_':"x",'=':"y",':':"z",'a':"1",'n':"2",'x':"3",'o':"4",
				'~':"5",'`':"6",'/':"7",'d':"8",'i':"9",'+':"0",'6':" ",'r':",",'c':".",' ':" "}
		mess=''
		for _ in range(0,len(jj)):
			mess = mess+ replace[jj[_]]
		ldscr()
		return mess
		#iyat=input()
################################################################################################################################################################3
def Anagram(text):
	print("   ###    ##    ##    ###     ######   ########     ###    ##     ## ")
	print("  ## ##   ###   ##   ## ##   ##    ##  ##     ##   ## ##   ###   ### ")
	print(" ##   ##  ####  ##  ##   ##  ##        ##     ##  ##   ##  #### #### ")
	print("##     ## ## ## ## ##     ## ##   #### ########  ##     ## ## ### ## ")
	print("######### ##  #### ######### ##    ##  ##   ##   ######### ##     ## ")
	print("##     ## ##   ### ##     ## ##    ##  ##    ##  ##     ## ##     ## ")
	print("##     ## ##    ## ##     ##  ######   ##     ## ##     ## ##     ## ")
	message=text #input("This will print all possible arrangements(permutations) of the word\nP.S. Heavy RAM user and May crash if lenght of word more than 9 letters.\n\nEnter word:")
	l=message.split(" ")
	perms = sorted(set(["".join(perm) for perm in itertools.permutations(message)]))
	n="./AnaGrams/"+message+".txt"
	f= open(n,"w")
	for i in range (len(perms)):
		if(perms[i]==message):
			f.write(str(i)+"."+perms[i]+"**")
			f.write("\n")
		else:
			f.write(str(i)+"."+perms[i])
			f.write("\n")
				
	f.close()
	fam=input("All anagrams have been saved in a file in \'AnaGrams\'")
################################################################################################################################################################3
def Hash(text):
	s=text
	md5=hashlib.md5(s.encode())
	sha224=hashlib.sha224(s.encode())
	sha1=hashlib.sha1(s.encode())
	sha256=hashlib.sha256(s.encode())
	sha384=hashlib.sha384(s.encode())
	sha512=hashlib.sha512(s.encode())
	ldscr()
	strr="\nMd5: " + md5.hexdigest() +"\nSHA224:" + sha224.hexdigest() + "\nSHA256:"+sha256.hexdigest()+"\nSHA384:"+sha384.hexdigest()+"\nSHA512:"+sha512.hexdigest()
	return strr
##############################################################################################################################################################

def ldscr():
	pass
	'''import time
	import os
	dods=0
	while dods<2:
		a=102
		b=1
		c=a+1
		for i in range(a+1,1,-1):
			print((i-1)*" ",(b)*"*")
			time.sleep(0.001)
			b=b+2

		for i in range(1,a+2):
			print((i-1)*" ",(b)*"*")
			time.sleep(0.001)
			b=b-2
		dods+=1
	os.system('clear')
	'''	    
################################################################################################################################################################3
def readMe():
	print("This program is made by Siddharth Johri and licenced under public domain.")
	print("These are some Requirements,Information and Suggestions for the use of this program.\n")
	print("General tip: Try to hide the Key/Shift information(If any) within the message such that it is legible.\n\nAnagram:\n1.Dont Use Spaces.Use the Serial numbers to your advantage.\n2.Dont input a words with more than 9 letters(Otherwise the time to process and the memory required may cause in a crash)\
		\n\nSubstitution:\n1.Dont use Numbers or symbols\n2.Trying to decrypt a message which has not been Encrypted using the specific key will result in error\
		\n\nReverseString:\nThis method is not secure as such...Pair it with another cipher for good quality cryptography.\
		\n\nRailFence:\nThis a very solid means of encryption.\nBe Sure to share the key with the one you are sending the message to.\
		\n\nCaesarEncryption:\nThis is a very elementary form of encryption where we just shift the letters of the alphabet.\nFor Best results use key/shift between 4 and 10\
		\n\nmd5:\nThis is the most secure way of encryption which also used to protect this program\nIt is used by most firms which store passwords.\nThis can not be decrypted, It can only be confirmed using a dictionary attack which can \nonly be exeuted if you have enough processing power.\
		\n\nSteganoGraphy:\nThe most sneaky form of encryption....\nHiding a message in a picture...\n1.Make sure the picture in which you want to hide the message is in the folder \"En\" inside \"Stego\".Create one if it is not there.\n\
2.Create a folder named Fresh inside Stego\n3.The picture which needs to be decrypted has to be placed in \'De\' inside Stego\n4.A picture which has no encryption will result in error if tried to decrypt\
		\n\nCasearBox:\nYet another cipher with the name of the legend....\nThe working is shown with the encryption\nUse as much punctuation as possible to make it very annoying for someone to try and decipher it by hand.\n\
		\nThis program is used to maintain privacy in this world of intrusion...\nUse it well\n\n\t\t\t\t\t\t\t\t\t\t\tLive Long and Prosper\n\n#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~#$_~")
	woah=input()
################################################################################################################################################################3
def SteganographyEncrypt():
	print("Move the Image to be encrypted to the file \"En\"\n")
	im = Image.open('./Stego/En/'+input("Enter name of file with extension:"))
	im.save('./Stego/En/Foto.png')
	file=("./Stego/En/Foto.png")
	message=input("Enter the message to be encrypted:")
	ldscr()
	f=lsb.hide(file,message)
	f.save("./Stego/Fresh/"+input("Enter name of new file with extension:"))
	print("Your file is saved in the folder \'Fresh\'")
	jj=input()

	pass
################################################################################################################################################################3
def SteganographyDecrypt():
	print("Move the image to\'De\'")
	file=input("Enter Filename with extension:")
	rev=lsb.reveal("./Stego/De/"+file)
	ldscr()
	print("The hidden message is:-\n"+rev)
	jh=input()
################################################################################################################################################################3

def Start():
	x=0
	while(x==0):
		passcode=input("\t\t\t\t\t\t\tThis is JoCrypt\n\t\t\t\t\tEnter Password To Continue:")
		h=hashlib.md5(passcode.encode())
		l=h.hexdigest()
		real = open("Pass.txt",'rU')
		rr=real.readlines()[0].strip()
		if(str(rr)==str(l)):
			os.system('clear')
			print("\n\n\t\t\t\t\t\tAccess Granted")	
			x+=1
		else:
			os.system('clear')
			print("\t\t\t\t\tAccess Denied\n\n")
			print(l)
			print(rr)
	l=input()
	pass  #
################################################################################################################################################################3
'''
def JoCrypt():
	#maximize_console()
	import sys
	import os

	print("                                                                                                                                                  ") 
	print("                                                                                                                                                  ")
	print("            JJJJJJJJJJJ                            CCCCCCCCCCCCC                                                                       tttt       ")  
	print("            J:::::::::J                         CCC::::::::::::C                                                                    ttt:::t         ") 
	print("            J:::::::::J                       CC:::::::::::::::C                                                                    t:::::t          ")
	print("            JJ:::::::JJ                      C:::::CCCCCCCC::::C                                                                    t:::::t          ")
	print("              J:::::J   ooooooooooo         C:::::C       CCCCCCrrrrr   rrrrrrrrryyyyyyy           yyyyyyyppppp   ppppppppp   ttttttt:::::ttttttt    ")
	print("              J:::::J oo:::::::::::oo      C:::::C              r::::rrr:::::::::ry:::::y         y:::::y p::::ppp:::::::::p  t:::::::::::::::::t    ")
	print("              J:::::Jo:::::::::::::::o     C:::::C              r:::::::::::::::::ry:::::y       y:::::y  p:::::::::::::::::p t:::::::::::::::::t    ")
	print("              J:::::jo:::::ooooo:::::o     C:::::C              rr::::::rrrrr::::::ry:::::y     y:::::y   pp::::::ppppp::::::ptttttt:::::::tttttt    ")
	print("              J:::::Jo::::o     o::::o     C:::::C               r:::::r     r:::::r y:::::y   y:::::y     p:::::p     p:::::p      t:::::t          ")
	print("  JJJJJJJ     J:::::Jo::::o     o::::o     C:::::C               r:::::r     rrrrrrr  y:::::y y:::::y      p:::::p     p:::::p      t:::::t          ")
	print("  J:::::J     J:::::Jo::::o     o::::o     C:::::C               r:::::r               y:::::y:::::y       p:::::p     p:::::p      t:::::t          ")
	print("  J::::::J   J::::::Jo::::o     o::::o      C:::::C       CCCCCC r:::::r                y:::::::::y        p:::::p    p::::::p      t:::::t    tttttt")
	print("  J:::::::JJJ:::::::Jo:::::ooooo:::::o       C:::::CCCCCCCC::::C r:::::r                 y:::::::y         p:::::ppppp:::::::p      t::::::tttt:::::t")
	print("   JJ:::::::::::::JJ o:::::::::::::::o        CC:::::::::::::::C r:::::r                  y:::::y          p::::::::::::::::p       tt::::::::::::::t")
	print("     JJ:::::::::JJ    oo:::::::::::oo           CCC::::::::::::C r:::::r                 y:::::y           p::::::::::::::pp          tt:::::::::::tt")
	print("       JJJJJJJJJ        ooooooooooo                CCCCCCCCCCCCC rrrrrrr                y:::::y            p::::::pppppppp              ttttttttttt  ")
	print("                                                                                       y:::::y             p:::::p                                   ")
	print("                                                                                      y:::::y              p:::::p                                   ")  
	print("                                                                                     y:::::y              p:::::::p                                  ")
	print("                                                                                    y:::::y               p:::::::p                                  ")
	print("                                                                                   yyyyyyy                p:::::::p                                  ")
	print("                                                                                                          ppppppppp   ")
	print("\n\nPress Enter to proceed to main menu")
	__________=input()	
	os.system('clear')
	x=0
	while(x==0):
		print("        ___  ___      _        ___  ___                 ")
		print("	|  \\/  |     (_)       |  \\/  |                 ")
		print("	| .  . | __ _ _ _ __   | .  . | ___ _ __  _   _ ")
		print("	| |\\/| |/ _` | | '_ \\  | |\\/| |/ _ \\ '_ \\| | | |")
		print("	| |  | | (_| | | | | | | |  | |  __/ | | | |_| |")
		print("	\\_|  |_/\\__,_|_|_| |_| \\_|  |_/\\___|_| |_|\\__,_|") #ASCII art to be finallised
		print("\n\nHello, this is Jodis. I will help you encode and encrypt")
		print("Choose the cipher with which you want to encrypt/decrypt a message")
		print("	\n1.Anagram\n2.Substitution\n3.ReverseString\n4.ReverseSubstitution\n5.RailFence(Encryption)\n6.RailFence(Decryption)\n7.CaesarEncrypt\n8.CaesarDecrypt\n9.Hash\n10.SteganographyEncrypt\n11.SteganographyDecrypt\n12.CaesarBoxEncrypt\n13.CaesarBoxDecrypt\nR for ReadMe and Instructions\nC for Credits\nQ to exit")				
		option=str(input("\n\n~$-"))  
		os.system('clear')
		if(option=="1"):
			Anagram()
			os.system('clear')
			#x+=1
		elif(option=="2"):
			Substitution()
			os.system('clear')
			#x+=1
		elif(option=="3"):
			ReverseString()
			os.system('clear')
			#x=+1
		elif(option=="4"):
			ReverseSubstitution()
			os.system('clear')
			#x=+1
		elif(option=="5"):
			encryptRailFence()
			os.system('clear')
		elif(option=="6"):
			decryptRailFence()
			os.system('clear')
		elif(option=="7"):
			CaesarEncrypt()
			os.system('clear')
		elif(option=="8"):
			CaesarDecrypt()
			os.system('clear')
		elif(option=="9"):
			Hash()
			os.system('clear')
		elif(option=="10"):
			SteganographyEncrypt()
			os.system('clear')
		elif(option=="11"):
			SteganographyDecrypt()
			os.system('clear')
		elif(option=="12"):
			BoxCipher()
			os.system('clear')	
		elif(option=="13"):
			BoxCipherDecryption()
			os.system('clear')
		elif(option=="C" or option=="c"):
			os.system('clear')	
			_=input()
			os.system('clear')
		elif(option=="R" or option=="r"):
			readMe()
			os.system('clear')
		elif(option=="Q" or option=="q"):
			os.system('clear')
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t    Live Long and Prosper")
			bye=input()
			sys.exit()
		else:
			print("Please enter a valid value\n\n")  
'''
#########################################################################################################################################################################
#Start()
if(__name__=="__main__"):
	JoCrypt()

