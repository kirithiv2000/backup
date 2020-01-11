def listshuffle(a):
    a[0],a[1],a[2]=a[2],a[1],a[0]
    return a
def righttoleft(a):
    for i in range(len(a)):
        a[i][0],a[i][2]=a[i][2],a[i][0]
    return a
def listd(a):
    for i in range(2):
        print(righttoleft(a))
        print(listshuffle(a))
def transpose(a):
    a[0][0],a[2][2]=a[2][2],a[0][0]
    a[0][1],a[1][2],a[1][0],a[2][1]=a[1][2],a[0][1],a[2][1],a[1][0]
j=[i for i in range(1,10)]
a=[[j[7], j[0], j[5]], [j[2], j[4], j[6]], [j[3], j[8], j[1]]]
listd(a)
transpose(a)
listd(a)
