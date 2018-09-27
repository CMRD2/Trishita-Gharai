print('Hii welcome to the game Snake and Ladder')
p1=0
while(p1<=100):
	b=input('press y to roll a die-')
	if(b=='y'):
		import random
		r=random.randint(1,6)
		print(r)
		p1=p1+r
		print('your position is-',p1)
	if(p1==100):
		print('you won...!!!')
		print('game over...!!!')
		break
	elif(p1==11):
		print('snake bite!!!')
		p1=2
		print('your position is-',p1)
	elif(p1==25):
		print('snake bite!!!')
		p1=4
		print('your position is-',p1)
	elif(p1==38):
		print('snake bite!!!')
		p1=9
		print('your position is-',p1)
	elif(p1==65):
		print('snake bite!!!')
		p1=40
		print('your position is-',p1)
	elif(p1==89):
		print('snake bite!!!')
		p1=70
		print('your position is-',p1)
	elif(p1==93):
		print('snake bite!!!')
		p1=64
		print('your position is-',p1)
	elif(p1==13):
		print('climb up the ladder')
		p1=34
		print('your position is-',p1)
	elif(p1==8):
		print('climb up the ladder')
		p1==37
		print('your position is-',p1)
	elif(p1==40):
		print('climb up the ladder')
		p1==68
		print('your position is-',p1)
	elif(p1==52):
		print('climb up the ladder')
		p1==81
		print('your position is-',p1)
	elif(p1==76):
		print('climb up the ladder')
		p1=98
		print('your position is-',p1)
	elif(p1>100):
		print("try again")
		p1=p1-r
		print('your position is-',p1)




	





