import os
import subprocess

basicTools = [
	'nmap'
]

moreTools = [
	'dirbuster'
]

install = 'sudo apt-get install '

print("[+] choice :")
print(" (1) - Basic tools")
print(" (2) - More tools")

if choice == 1:
	for tool in basicTools:
		os.system(install+tool)
elif choice == 2:
	for tool in basicTools:
		os.system(install+tool)
	for tool in moreTools:
		os.system(install+tool)
else:
	print("You need to choose between 1 or 2")
