import os

file1=open("4b44b334ac0ff0a281597fb66c6f78bc8f5d537e_file1.txt", "r").read()
file2=open("d1de718973b070b1c12b78cef89d21ded505f9f0_file2.txt", "r").read()

u=zip(file1,file2)
flag=""
for i,j in u:
	if i==j:
		continue
	else: 
		flag=flag+i

print flag[::-1]


