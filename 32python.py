a=['1','2','3','4','5','6','7','8','9']
def table():
    print("---------")
    print("|",a[0],"|",a[1],"|",a[2])
    print("---------")
    print("|",a[3],"|",a[4],"|",a[5])
    print("---------")
    print("|",a[6],"|",a[7],"|",a[8])
playerOneTurn = True
while True:
	table()
	p=input("choose an available place : ")         

	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='0'):
			print("Place taken, choose another place ...")
			continue
		else:
			if playerOneTurn:
				print("Player 1>>")
				a[int(p)-1] = 'X'
				playerOneTurn = not playerOneTurn
			else:
				print("player 2 >>")
				a[int(p)-1] = 'o'
				playerOneTurn = not playerOneTurn
			for i in (0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game Over...")
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over...")
					exit()	
	else:
		continue