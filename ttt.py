# tic tac toe
a=['1','2','3','4','5','6','7','8','9']

def board():
	print('-------------')
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print('-------------')
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print('-------------')
	print('|',a[6],'|',a[7],'|',a[8],'|')
	print('-------------')


p1 = True
while True:
	board()
	c=input('Choose your position')
	if(c in a):
		if(a[int(c)-1]=='x' or a[int(c)-1]=='o'):
			print('Choose a different position')
			continue
		else:
			if p1:
				print('Player1-')
				a[int(c)-1] = 'x'
				p1 = not p1
			else:
				print('Player2-')
				a[int(c)-1] = 'o'
				p1 = not p1
		for i in range(0,3,6):
			#row check
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				print("game over!!!!")
				exit()
		for i in range(3):
			#coloumn check
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				print("game over!!!!")
				exit()
		#diagonal check
		if(a[0]==a[4] and a[0]==a[8]):
			print("game over!!!!")
			exit()
		if(a[2]==a[4] and a[2]==a[6]):
			print("game over!!!!")
			exit()	
	if(c not in a):
		print('invalid')	
		continue
	else:
		print('Tie')
		exit()
