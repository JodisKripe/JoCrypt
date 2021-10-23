import sys
import os
import subprocess

packagesToInstall = ['ctypes','PIL','itertools','hashlib','stegano']

print("\tUpdating pip...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install','-U', 'pip'])

print("\n \tInstalling packages...\n")
for i in packagesToInstall:
	subprocess.run([sys.executable, '-m', 'pip', 'install', i])
	print("\nInstalled ", i, "\n")

os.system("echo.")
print("Installed packages:\n")
subprocess.run([sys.executable, '-m', 'pip', 'freeze'])
os.system("echo.")
os.system("pause")
