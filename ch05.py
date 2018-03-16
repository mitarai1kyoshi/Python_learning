#if语句
a=25
b=[1,5,6,9,18,20]
if a>=0 and a<=10:
    print("smaller than 10")
elif a<20:
    print("bigger than 10,smaller than 20")
else:
    print("bigger than 20")
if a not in b:   #查找
    print("not found 5")
print(a==b[1])#bool
#确定列表不为空
names=[]
if names:
	if tom in names:
		print("found")
	else:
		print("not found")
else:
    print("null")

current_users=['tom','tony','jack','amy','anny']
new_users=['Jack','Alice']
for i in new_users:
	if i.lower() in current_users:
		print("used,please changed")
	else:
		print("name is ok")