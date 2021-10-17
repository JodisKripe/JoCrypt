#py2exec A utility mainly to get a single file in which you can fit the program.
import os


def make(file):
    string="pyinstaller --onefile "+file
    os.system(string)


file=input("Enter the file to convert to .exe format:")

make(file)