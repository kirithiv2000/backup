# p=[2,3,5,7,11,13,17,23]
# a=int (input("enter a prime number"))
# l=len(p)
# b=0
# while b<l:
# 	if p[b]==a:
# 		print(a,"is",b,"th number in prime numbers")
# 	b+=1



# a=int(input("enter a prime number"))
# b=0
# c=2
# d=2
# while c<=a:
# 	d=2
# 	while c>d:
# 		if c%d==0:
# 			break
# 		d+=1
# 	else:
# 		print (c)
# 		b+=1
# 	c+=1
# 	print(c-1,"is",b,"th number in prime numbers")
# year = 2016
# name = "NavGurukul"
# print (name , ', ' ,year ," mein start hua tha!")]


# a=[1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
# l=len(a)
# b=0
# while b<l:
# 	e=a[b]
# 	if c<=e:
# 		c=e
# 		break
# 	b+=1	

# def k():
# 	for i in range(8):
# 		for j in range(5):
# 			if (j is 0) or ((i+j is 4) or (i-j is 3 )):
# 				print("*",end=" ")
# 			else:
# 				print(" ",end=" ")
# 		print()

# def i():
# 	for i in range(8):
# 		for j in range(5):
# 			if (i is 0) or ((i is 7) or (j is 2)):
# 				print("*",end=" ")
# 			else:
# 				print(" ",end=" ")
# 		print()
# def r():
# 	for j in range(8):
# 		for i in range(5):
# 			if ((j is 0) or (i is 0)) or((i is 4) and (j<4)) or ((j==3) and (j < 4)) or (j-i ==3):
# 				print("*",end=" ")
# 			else:
# 				print(" ",end=" ")
# 		print()

# def h():
# 	for i in range(8):
# 		for j in range(5):
# 			if ((j is 0) or (i is 4)) or (j is 4):
# 				print("*",end=" ")
# 			else:
# 				print(" ",end=" ")
# 		print()	

# def v():
# 	for i in range(5):
# 		for j in range(9):
# 			if ((i is j) or (i+j is 8)):
# 				print("*",end="")
# 			else:
# 				print("",end=" ")
# 		print()	

# def t():
# 	for i in range(8):
# 		for j in range(5):
# 			if (i is 0)  or (j is 2):
# 				print("*",end=" ")
# 			else:
# 				print(" ",end=" ")
# 		print()
			


# k()
# print(" ")
# i()
# print(" ")
# r()
# print(" ")
# i()
# print(" ")
# t()
# print(" ")
# h()
# print(" ")
# i()
# print(" ")
# v()

# for i in range(8):
# 	for j in range(9):
# 		if (i == 0 and j % 2 is 1) or (i == 1 and j % 2 is 0) or ((i is 2 and j % 2 is 1) and (j>4)) or ((i == 3 and j % 2 is 1) and (j<4)) or (i+j is 9 and i > 4) or (i-j is 1 and i > 4) or ((j is 2 or j is 6 ) and i != 0):
#  				print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# a=int(input(" number"))
# print("binary number of",a,"is ",(a))



# a=input("decimal number")
# for i in range(10):
# 	if int(a)>0:
# 		print(int(a)%2)
# 		a=int(a)//2
# 		a=str(a)




# a=input("enter decimal number")
# for i in range(10):
# 	a=int(a)
# 	if a>0:
# 		print(a%2)
# 	a=a//2


# a=str(input("any binary u know"))
# b=len(a)
# binary=[1,0]
# c=0
# d=0
# e=[]
# while c<b :z
# 	if a is binary():
# 		d=int(a[c])*(2**c)
# 		e.append(d)
# 		c+=1
# print(sum(e))

# a=int(input(" number"))
# print(0b+a)

# a=int(input("enter number"))
# print(bin(a)[2:])

# import getpass
# a=getpass.getpass('what is your password')
# if a=='kirithiv':
# 	print('congrats')
# else:
# 	print('incorrect password')






# list1 = [1,3,54,5]

# def sum1(list1):
# 	# print(sum(list1))
# 	return sum(list1)

# print(sum1(list1))


# def sun():
# 	w = sum1(list1)
# 	print(w)

# sun()

# import random
# import getpass
# game_list=["stone","paper","scissor"]
# def player():
# 	print("you win "+computer1 + "-"+player1 + " you got ", p ," points")

# def computer():
# 	print("you lost "+computer1+"-"+player1+" computer got ",c," points")



# c=0
# p=0
# a=2
# while c<a or p<a:
# 	computer1=random.choice(game_list)
# 	# print(computer1)
# 	player1=getpass.getpass("choose your stone/paper/scissor").lower()
# 	print("my choice - your choice")
	
# 	if computer1==player1:
# 		print("we both think same ("+player1+")")
# 		continue
# 	if computer1=="paper" and player1=="scissor":
# 		p+=1
# 		player()
# 	if computer1=="stone" and player1=="paper":
# 		p+=1
# 		player()
# 	if computer1=="scissor" and player1=="stone":
# 		p+=1
# 		player()	
# 	if computer1=="paper" and player1=="stone":
# 		c+=1
# 		computer()
# 	if computer1=="stone" and player1=="scissor":
# 		c+=1
# 		computer()
# 	if computer1=="scissor" and player1=="paper":
# 		c+=1
# 		computer()
# 	if p==a:
# 		print("user wins")
# 		n=input("do you want to play more press m or press any key to exit other than m ")
# 		if n=="m":
# 			a+=2
# 		else:
# 			break
# 	if c==a:
# 		print("user lost")
# 		n=input("do you want to play more press m or press any key to exit other than m ")
# 		if n=="m":
# 			a+=2
# 		else:
# 			break

		
# else:
# 	print("thank you for playing")
