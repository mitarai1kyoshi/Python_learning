#变量 数据类型
name = 'Hello Python   '   #//f: ,cd pwork  ,python 1.py
print(name.upper())#不改变name值  print(name.lower())
name_modified=name.rstrip()#去除末尾多余的空白,也可以用lstrip,strip去除开头和两端的空白

age=18
message="happy "+str(age)+"th birthday"  #int to string
print(message)