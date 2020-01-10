# def pivots_position(list1,first,last):
# 	pivot=list1[first]
# 	left=first+1
# 	right=last
# 	while 1:
# 		while left<=right and list1[left]<=pivot:
# 			left+=1
# 		while right>=left and pivot<=list1[right]:
# 			right-=1
# 		if left>right:
# 			list1[first],list1[right]=list1[right],list1[first]
# 			break
# 		else:	
# 			list1[left],list1[right]=list1[right],list1[left]
# 	return right

# def quick_sort(list1,first,last):
# 	if first<last:
# 		p=pivots_position(list1,first,last)
# 		quick_sort(list1,p+1,last)
# 		quick_sort(list1,first,p-1)
		
# import random
# a=[random.randint(1,100) for i in range(100)]
# quick_sort(a,0,len(a)-1)
# print(a)


# a='[({{{{}}}})][({}())}]'
# a=input()
# # a='[({{}})]'
# # a='{{{}}}[[()]]'
# dic={'[':']','(':')',"{":"}"}
# bracket=0
# varBracket=''
# howManyFalse=[]
# for i in a:
# 	if i in dic:
# 		bracket+=1
# 		varBracket+=i
# 	if i in dic.values():
# 		bracket-=1
# 		if varBracket!='':
# 			if i!=dic[varBracket[-1]]:
# 				howManyFalse.append(False)
# 				break
# 			else:
# 				if varBracket!='':
# 					varBracket=varBracket[:-1:]
# 				else:
# 					howManyFalse.append(False)
# 					break
# 		else:
# 			howManyFalse.append(False)
# 			break



# if varBracket=="":
# 	if howManyFalse==[]:
# 		print(True)
# 	else:
# 		print(False)
# else:
# 	print(False)

	# print(bracket,i)


# Remove friend Algorithm
 
# # Iterating loop for taking inputs
# for i in range(int(input())):
#     n,k=[int(y) for y in input().split()]
#     friend=[int(y) for y in input().split()]
#     temp=[]
#     f=False
#     # Iterating loop on friend list
#     for j in friend:
#         while temp and temp[-1] <j and k!=0:
#             # removing first friend if second friend popularity is more than first.
#             temp.pop()
#             k = k-1
#             f=True
#         # If temp is empty.
#         temp.append(j)          
#     if f==False:
#         # If all friends are less polpular than first then it remove the last friend fro the list
#         temp.remove(temp[-1])
#     print(" ".join(map(str,temp)))


# # Function for sum of the distance between two coordinates
 
# def distance (arr, n): 
      
#     # sorting the array. 
#     arr.sort() 
    
#     result = 0
#     sum = 0
#     for i in range(n): 
#         result += (arr[i] * i - sum) 
#         sum += arr[i] 
#     return result 
 
# #providing inputs for program    
# n = input()
# n =int(n)
# x = []
# y = []
# for i in range(0, int(n)):
#    x_input, y_input = input().split(' ')
#    x.append(int(x_input))
#    y.append(int(y_input))
  
# # calling the function  
# print(distance(x, n) + distance(y, n)) 
 
'''
 
First I think this logic to solve but it gives memory error so i have changed my thinking and used maths to solve this problem
 
from itertools import combinations

list_1 = []
list_2 = []
for i in range(int(input())):
    a = (input().split())
    list_1.append (int(a[0]))
    list_2.append (int(a[1]))
    
def pairs(arr, r): 
    return list(combinations(arr, r))
  
# Driver Function 
b = pairs(list_1, 2) 
c = pairs(list_2, 2)
 
result = 0
 
for i in range (len(b)):
    x = abs(b[i][0] - b[i][1])
    y = abs(c[i][0] - c[i][1])
    result = result + x + y
print (result) '''







def range(startingNumber,endingNumber=10,differanceNumber=1):
	if startingNumber>endingNumber-1:
		return []
	value=range(startingNumber+differanceNumber,endingNumber,differanceNumber)
	value.insert(0,startingNumber)
	return value
print(range(1,6))   #[1, 2, 3, 4, 5]
print(range(0,20,))#[0, 2, 4, 6, 8]
print(range(1,10,2))#[1, 3, 5, 7, 9]

# if i in range(10)



