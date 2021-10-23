import sys
import os
import subprocess

packagesToInstall = ['ctypes','PIL','itertools','hashlib','stegano']
subprocess.check_call([sys.executable, '-m', 'pip', 'install','-U', 'pip'])

for i in packagesToInstall:
	os.system("pip install %s" %(i))
	try: 
		reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
		installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
		if(i in installed_packages):
			print("Installed ", i)
			os.system("pause")
	except subprocess.CalledProcessError as e:
		raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

os.system("pause")

'''
for i in packagesToInstall:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
	reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
	installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

'''
