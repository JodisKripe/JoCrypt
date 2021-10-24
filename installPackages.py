import sys
import os
import subprocess

packagesToInstall = ['ctypes','PIL','itertools','hashlib','stegano']

print("Updating pip...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install','-U', 'pip'])

print("\nInstalling packages...\n")
for i in packagesToInstall:
	subprocess.run([sys.executable, '-m', 'pip', 'install', i])
	print(i,"is ready to use!")
	
print("\nInstalled packages:")
os.system("python -m pip freeze & pause")
