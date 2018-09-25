def greet(name):
	if(name):
		print("hello",name)
	else:
		print("hello global")
	return
name=(input("tell me your name-"))
greet(name)