board=["_","_","_",
	   "_","_","_",
	   "_","_","_"]

a=("~~~~~~~")
b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


board1=[a,b,c,d,a]
for i in board1:
	print(i)
player1choice=[]
player2choice=[]
win=" "

#gameisgoing
gameisgoing=True
import random
while gameisgoing:
	player1=int(input(" CHOOSE THE POSITION 1-9  playerx:"))
	if player1 not in player1choice and player1 not in player2choice:
		board[player1-1]="x"
		player1choice.append(player1)
		a=("~~~~~~~")
		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"

		board1=[a,b,c,d,a]
		for i in board1:
			print(i)
			
		horizondal=[]
		h=""
		for i in range(len(board)):
			h+=board[i]
			if len(h)==3:
				horizondal.append(h)
				h=""
		for i in horizondal:
			if i=="xxx":
				print("playerx is the winner")
				win="playerx is the winner"
				break
		if i=="xxx":
			
			break
		vertical=[]
		for i in range(3):
			v=""
			v+=board[i]+board[i+3]+board[i+6]
			vertical.append(v)	


		for i in vertical:
			if i=="xxx":
				print("playerx is the winner")
				win="playerx is the winner"
				break
		if i=="xxx":

			break
		diagonal=[]
		diagonal.append(board[0]+board[4]+board[8])
		if diagonal[0]=="xxx":
			print("playerx is the winner")
			win="playerx is the winner"
			break

			
		andiagonal=[]
		andiagonal.append(board[6]+board[4]+board[2])
		if andiagonal[0]=="xxx":
			print("playerx is the winner")
			win="playerx is the winner"

			break

		if "_" in board:
			pass
		else:
			win="MATCH TIE"
			print("MATCH TIE")
			gameisgoing=False

			break
	else:
		print("\v\vThat place is already CHOOSEen")

	player2=int(input(" CHOOSE THE POSITION 1-9  playero:"))
	if player2 not in player2choice and player2 not in player1choice:
		board[player2-1]="o"
		player2choice.append(player2)
		a=("~~~~~~~")
		b="|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
		c="|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
		d="|"+board[6]+"|"+board[7]+"|"+board[8]+"|"

		board1=[a,b,c,d,a]
		for i in board1:
			print(i)

		horizondal=[]
		h=""
		for i in range(len(board)):
			h+=board[i]
			if len(h)==3:
				horizondal.append(h)
				h=""
		for i in horizondal:
			if i=="ooo":
				print("playero is the winner")
				break
		if i=="ooo":
			win="playero is the winner"
			
			break
		vertical=[]
		for i in range(3):
			v=""
			v+=board[i]+board[i+3]+board[i+6]
			vertical.append(v)	

		for i in vertical:
			if i=="ooo":
				print("playero is the winner")
				break
		if i=="ooo":
			win="playero is the winner"

			break

		diagonal=[]
		diagonal.append(board[0]+board[4]+board[8])
		if diagonal[0]=="ooo":
			win="playero is the winner"
			print(win)

			break

			
		andiagonal=[]
		andiagonal.append(board[6]+board[4]+board[2])
		if andiagonal[0]=="ooo":
			win="playero is the winner"
			print(win)

			break

		if "_" in board:
			pass
		else:
			win="MATCH TIE"
			print("MATCH TIE")
			gameisgoing=False
			break

	else:
		print("\v\vThat place is already CHOOSEen")
