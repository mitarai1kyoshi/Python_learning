#列表
name=['tom','anny','ammy','tod','suzuki','toyota']
print(name[-2].title())  #列表长度未知时打印倒数第二个
message1="My best friend is "+name[0].title()+"."#print(message1)

name.append('jack')#末尾增加 print(name[-1])
name.insert(2,'zhang') #2位置插入
del name[3]#delete 2rd element print(name[2])

gotname1=name.pop()#pop the last element
gotname2=name.pop(1) #different from del
name.remove('zhang')#删除第一个指定的值
 
#name.sort()
#name.sort(reverse=True) #反向排序
names=sorted(name)#name remained unchaged
names.reverse()
le=len(names)

for i in names:
    print(i.title()+" is a friend of mine.")
for v in range(1,6)#print 1-5
    print(v)
even=list(range(2,13,2))#2-13的奇数存入list 
#min(even)    max(even)    sum(even)

#列表解析
cube=[value**3 for value in range(1,11)]#x**3 乘方

myfriend=names[:]#copy
r=copy.deepcopy(rs)  #如果列表里还有其他非基本数据类型
#myfriend=names  #they are the same

#元组 元素不可修改，但整体可以修改,其他操作不变
tmp=(23,4,5,1)
tmp=(23,5,6,7)