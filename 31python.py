import random

c={1:'r',2:'p',3:'s'}
a=input("enter r or p or s")
s=random.choice(d)
if(a==s):
	print("tie play again")
elif(s=='r'):
	if(a=='p'):
		print("p win")
	else:
		("a win")
elif(s=='p'):
	if(a=='s'):
		print('s win')
	else:
		("c wins")