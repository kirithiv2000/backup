import math
d={0:0}
def trianglen(a):
    if a-1 in d:
        b=a+d[a-1]
        d[a]=b
        # print(b)
        return b
    b=0
    for i in range(1,a+1):
        b+=i
    # print(b)
    return b
def tnfactor(a):
    a=trianglen(a)
    # a=76576500
    b=[]
    sq=int(math.sqrt(a))
    for i in range(1,sq+1):
        if a%i==0:
            b.append(i)
            if i!=sq:
                b.append(a//i)
    # print(b,end="\r")
    return len(b)-1,b
count=1
while 1:
    count1=tnfactor(count)
    if count1[0]>=500:
        print(count1)
        break
    # print(count,count1,end="\r")
    # print(count1,"cout")
    count+=1

# print(tnfactor(7))
# print(tnfactor())

