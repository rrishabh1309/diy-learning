import os
import random

print("!!!! SCRIPT STARTED !!!!")

os.chdir('D:/Github/diy-learning/')
os.system('ls')
os.system('git pull')
os.system('git add --all')
os.system('git commit -am "updated script"')

with open("input.txt", 'r') as fp:
	digits = fp.read()

fp.close()

START = int(digits)
DIFF = random.randint(10, 20)
END = START + DIFF

# Create files
for i in range(START, END):
	filename = 'out//' + str(i) + '.txt'
	with open(filename, 'w') as fp:
		fp.write(str(i))

# git commands
for i in range(START, END):
	add_command = 'git add ' + 'out//' + str(i) + '.txt'
	print(add_command)
	os.system(add_command)
	commit_message = 'Adding file ' + str(i) + '.txt'
	commit_command = 'git commit -m ' + '"' + commit_message + '"'
	print(commit_command)
	os.system(commit_command)

# push command
os.system('git commit -am "minor refactoring"')
os.system('git push')

with open("input.txt", 'w') as fp:
	fp.write(str(END))

fp.close()

print("!!!! SCRIPT FINISHED !!!!")
