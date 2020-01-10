# a=[1,2,3,4,5,6,7,8,100,1000,9,99,999,888,777,555,1111111,222,222222222,44444466666666,333334444111]
# # t=True
# # while t:
# # 	g=1
# # 	c=0
# # 	while c<len(a)-1:
# # 		if a[c]>a[c+1]:
# # 			a[c],a[c+1]=a[c+1],a[c]
# # 		else:
# # 			g+=1
# # 			if g==(len(a)-1):
# # 				t=False
# # 		c+=1
# # print(a)
# c=0
# b=0
# while 1:						#True condition
# 	if b==len(a)-1:				#b==11 condition 
# 		b=0						#b = 0 and
# 		c=0						#c = 0
# 	if a[b]>a[b+1]:				#1st num>2nd num condition
# 		a[b],a[b+1]=a[b+1],a[b] #swaping
# 	else:						
# 		c+=1					#incriment of c
# 	b+=1						#incriment of b
# 	c+=1						#incriment of c
# 	if c==2*(len(a)-1):			#c == 22 condition
# 		break					#end the loop
# # print(a)
	
# import pprint
# d={i:i**2 for i in range(1,6)}  #key is number and value is its square
# # pprint.pprint(d)

# d={i:[i for i in range(i,i*11,i)] for i in range(1,6)} #key is num and value is a list of num on key's table
# pprint.pprint(d)



# aa=int(input())
# a=aa
# b=[i for i in range(1,a+1) for j in range(i)]
# print(b)
# # 1
# # 3 2
# # 4 5 6
# # 10 9 8 7
# # 11 12 13 14 15
# # 21 20 19 18 17 16
# # ** ** ** ** 23 22
# bb=[i for i in range(1,aa+1)]
# # print(b)
# # print(bb)
# c=bb.index(bb[-1])
# d=b[c+1:]
# e=d.count(b[c])
# for i in range(e):
# 	bb.append("*"*len(str(bb[c]+i)))
# # print(bb)
# o=0
# p=0
# while o < len(bb)-1:
# 	if p%2==0:
# 		for i in range(p+1):
# 			print(bb[o],end=" ")
# 			o+=1
# 		print()
# 	else:
# 		l=[]
# 		for i in range(p+1):
# 			l.append(bb[o])
# 			o+=1
# 		l=l[::-1]
# 		for i in l:
# 			print(i,end=" ")
# 		print()
# 	p+=1


# a=int(input())
# for i in range(a+1):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print()


# a=int(input("enter 1st no"))
# print "enter operator"
# opp=int(input())
# b=int(input("enter 2nd no"))
# if opp==addition:
# 	print (addition)
# elif opp==subtraction:
# 	print (subtraction)
# elif opp==multiply:
# 	print (multiply)
# else:
# 	print (division)
# a=int("enter no")
# if a%3==0:
# 	print "fizz"
# elif a%7:
# 	print "buzz"
# elif a%7==0 and a%3==0:
#     print "fizz buzz"
# else:
# 	print "not divisble"

#-----------------------------------------------------------------------------------------------------
# user=int(input("enter the number:"))
# user1=int(input("enter the number:"))
# a=1
# while a<user:
# 	user+=user1
	
# print(user)
# a+=1
#------------------------------------------------------
# a=[[1],[2],[3]]
# user=int(input("enter"))
# a=[]
# for i in range(1,11):
# 	a.append(i)
# 	b=[]
# 	for j in range(1,11):
# 		b.append(i*j)
# 	a.append(b)
# print(a)
#----------------------------------------------------------------------------------------------------------
# a=[5,4,24,8,-10,11]
# max1=0
# for i in a:
# 	if i>max1:
# 		max1=i
# max2=1

# for j in a:
# 	if j>max2 and max1!=j:
# 		max2=j
# print(max2)
#---------------------------------------------------------------------------------------------------
# a=[5,4,6,1,2]
# for i in a:
# 	for j in range(len(a)-1):
# 		if a[j]>a[j+1]:
# 			a[j],a[j+1]=a[j+1],a[j]
# print(a)
#------------------------------------------------------------------------------
# user=int(input("enter"))
# a=[]
# c={}
# for i in range(1,user+1):
# 	a.append(i)
# 	b=[]
# 	for j in range(1,11):
# 		b.append(i*j)
# 	c[i]=b
# print(c)




# for i in range(int(input('enter no.'))):
# 	i+=3
# 	print(i)

# i=0
# while i<int(input('enter no')):
# 	i=i+3
# 	print(i)
# 	
# b=0
# sum=0
# while True:
# 	a=int(input())
# 	if b==0:
# 		c=a
# 	else:
# 		sum+=a
# 		if b==c:
# 			print(sum)
# 			break
# 	b+=1

# s=0
# i=0
# l=''
# while True:
# 	k=int(input('enter no'))
# 	l+=str(k)
# 	s+=k
# 	if int(l[0])==i:
# 		break
# 	i+=1
# print(s-int(l[0]))