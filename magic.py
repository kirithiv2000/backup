w=[]
for i in range(31):
    w.append([0 for i in range(31)])
w=[[0,0,0],[0,0,0],[0,0,0]]
w=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
w=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
w=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

turn=0
side=len(w)//2
start=25

while 1:

    if w[turn][side]==0:
        changes=0
        w[turn][side]=start

        if turn == 0:
            turn =len(w)-1
        else:
            turn -=1
        if side ==len(w)-1:
            side =0
        else:
            side+=1
        start +=1
    else:
        if turn ==len(w)-1:
            turn =1
        elif turn ==len(w)-2:
            turn =0
        else:
            turn +=2
        if side !=0:
            side -=1
        else:
            side +=len(w)-1
        changes+=1
        if changes>5:
            break

for i in w:
    print(i)
