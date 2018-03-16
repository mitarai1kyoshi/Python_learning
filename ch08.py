# 函数 
#默认参数必须指向不变对象 否则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
import car as mycar
def add_end(L=None):
	if L is None:
		L=[]
	L.append('end')
	return L
	
def make_album(singer_name,album_name,num=0):
	if num:
		album={'singer':singer_name,'album':album_name,'num':num}
	else:
		album={'singer':singer_name,'album':album_name}
	return album
print(make_album('tom','my love'))

#可变参数
def sum(*num):  #参数num接收到的是一个tuple
	summ=0
	for i in num:
		summ=summ+int(i)
	return summ
num=[1,2,3,4,5]
print(sum(*num))#转化

#**表示可以接收任意数量的参数  到时候创建dict
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 45, gender='M', job='Engineer') #使用必须指明key

#命名关键字参数需要*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')#必须传入参数名

mycar.car('sabaru','outback',color='blue',money=1234)