while True:
	a=(input("press y to roll the dice"))
	if(a=="y"):
		import random
		r=random.randint(1,6)
		print(r)
	else:
		print("tata, bye bye")
		break