#  input & while
name=input("input your name:")  #默认字符串
age=input("how old are u? ")
age=int(age)
if age>=18:
	print(name+" is not a kid")

names=['tom','tod','tommy','tod']
new=[]
while names:
	current_name=names.pop()  #pop可删除任意位置
	new.append(current_name)
while 'tod' in new:
	new.remove('tod')   #如果知道位置可以用del names[]
print(new)