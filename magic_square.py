import string
import random
def check(allsum):
	import string
	if allsum=="":
		return False
	al=list(allsum)
	z=len(al)
	count=0
	s=[i for i in string.digits]
	for i in al:
		if i in s:
			count+=1
	if count==z:
		return True
	return False

def magic_square(a):
	horizondal=[]
	vertical=[]
	diagonal=[]
	antidiagonal=[]
	for i in a:
		horizondal.append(sum(i))
	for i in range(len(a)):
		diagonal.append(a[i][i])
	l=2
	for i in range(len(a)):
		antidiagonal.append(a[i][l])
		l-=1
	for i in range(len(a)):
		b=[]
		for j in a:
			b.append(j[i])
		vertical.append(sum(b))
	if horizondal[0]==horizondal[1]==horizondal[2]==vertical[0]==vertical[1]==vertical[2]==sum(diagonal)==sum(antidiagonal):
		print("magic_square")
		for i in a:
			print(i)
		return True
	return False
def randomly_created_magic_square():
	allsum=input("(MAGIC SQUARE) ENTER A NUMBER FROM 3'S TABLE :")
	if not check(allsum):
		print("please enter a number")
	elif(int(allsum)%3 != 0):
		print("Please Enter the number comes under the 3's table")
	else:
		allsum=int(allsum)
		while 1:
			start=allsum//3-4
			end=allsum//3+5
			No_in_magic_square=[i for i in range(start,end)]
			zz=[]
			for i in range(3):
				z=[]
				for j in range(3):
					g=random.choice(No_in_magic_square)
					No_in_magic_square.remove(g)
					z.append(g)
				zz.append(z)

			if magic_square(zz):
				break

randomly_created_magic_square()
