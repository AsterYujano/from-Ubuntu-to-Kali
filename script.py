import os
import subprocess

basicTools = [
	'nmap',
	'curl',
	'dirb',
	'exiftool',
	'steghide'
]

moreTools = [
	'wifite',
	'aircrack-ng',
	'reaver',
	'bully',
	'metasploit',
	'armitage',
	'wireshark'
]

install = 'sudo apt-get install '

print("\n|------------------------------|")
print("|  If you need Kali tools...   |")
print("| ...But you only have Ubuntu  |")
print("|------------------------------|")
print(" [+] Choice between :")
print(" (1) - Basic tools")
print(" (2) - More tools")

print("\n_______________________")
print("Basic tools : ")
for tool in basicTools:
		print(tool+" ", end=" ")
print("\n_______________________")
print("All the basic tools, more :")
for tool in moreTools:
		print(tool+" ", end=" ")
print("\n_______________________")
print("What do you choose ?")


choice = input()

if choice == "1":
	for tool in basicTools:
		os.system(install+tool)
elif choice == "2":
	for tool in basicTools:
		os.system(install+tool)
	for tool in moreTools:
		os.system(install+tool)
else:
	print("You need to choose between 1 or 2")
