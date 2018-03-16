#字典 不按输入顺序存储
myself={'name':'zhang','age':22}
myself['sex']='girl'
del myself['sex']
print("My name is "+
	myself['name']+". I'm "+str(myself['age'])+
	" years old.")
friend={'tao':'high school','gao':'university','tan':'graduate'}
#遍历键值对
for k,v in friend.items():
	print(k+" "+v)
#for k in friend.keys():   遍历所有键
#for k in sorted(friend.keys())	:  按顺序遍历所有键
for v in friend.values():
	print(v)
#字典组成列表
family=[]
father={'name':'zhang','age':48}
mother={'name':'li','age':47}
family.append(myself)
family.append(father)
print(family)