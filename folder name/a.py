
# def char_frequency(str1):
#     dict = []
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency("23456sdfghbnmnbvcxsrtyu12@#$"))


usre=input("enter")
lis=[]
count=0
for i in usre:
	for j in i:
		if j in i:
			count=j+i
			lis.append(count)
print(lis)
