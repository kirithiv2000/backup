l=[]
def align(n1):
	if len(l)>=2:
		for i in range(len(l)):
			if l[i]<n1:
				pass
			else:
				l.insert(i-1,n1)
	elif len(l)==1:
		if l[0]<n1:
			l.append(n1)
		else:
			l.insert(0,n1)
	else:
		l.append(n1)
	print(l)
	

def sep(lsit,first,last):
	first=0
	last=len(lsit)-1
	mid=((first+last)//2)+1
	if len(lsit)>1:
		print(sep(lsit[:mid],first,mid-1),sep(lsit[mid:],mid,last))
		return (lsit[:mid]+lsit[mid:])
	return align(lsit[0])


a=[55,3,2,44,22,11,32,12,8,79]
sep(a,0,len(a)-1)
# print(a)