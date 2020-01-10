# a=1
# while a<=100:
# 	if a%2==0:
# 		print(-a)
# 	else:
# 		print(a)
# 	a=a+1


# a=100
# b=2
# while a>0:
# 	print (a)
# 	print(-b)
# 	a=a-2
# 	b=b+2



# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))


a=[1,2]
b=[3,4]
a.extend(b)
print(a)
print(b)
