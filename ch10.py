#文件
filename = 'example.txt'
with open(filename) as file_object:
	#contents = file_object.read()
	#print(contents.rstrip())  #删除末尾的空白
	for line in file_object:
		print(line.rstrip())

try:		
	with open('example.txt') as file_object:
		lines = file_object.readlines()
except FileNotFoundError:
	#pass     #这里什么都不做
	print("sorry")
	
tmp=''	
for line in lines:
	print(line.rstrip())
	tmp = tmp + line.rstrip()
print(tmp)
print(tmp.replace('include','python'))

with open(filename,'w') as file_object:
	file_object.write('clear  the file\n')
	
with open(filename,'a') as file_object:
	for n in range(1,3):
		line = input("input ur name: ")
		file_object.write(line+'\n')
		
#异常
#try except else
num1 = input("input a num: ")
num2 = input("input another num: ")
try:
	answer = int(num1) / int(num2)
except ZeroDivisionError:
	print("!")
else:
	print(answer)
	
#存储数据
import json
num=[2,3,5,7]
filename = 'num.json'
with open(filename, 'w') as f_obj:
	json.dump(num, f_obj)
	#numbers=json.load(f_obj)
