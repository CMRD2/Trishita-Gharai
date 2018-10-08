#ROCK PAPER SCISSOR
print("hi...! lets play rock paper scissors :D")
s1=0
s2=0
while(s1<=3 or s2<=3):
	a=input('enter choice(rock-r,paper-p,scissor-s)-')
	import random
	d=['r','p','s']
	s=random.choice(d)
	print(s)
	if(a==s):
		print('draw...')
		print(s1)
		print(s2)
	elif(s1==3):
		print('you win')
		break
	elif(s2==3):
		print('you lose')
		break
	elif(a=='p' and s=='r'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='p' and s=='s'):
		print('try')
		s2=s2+1
		print(s1)
		print(s2)
	elif(a=='s' and s=='r'):
		print('try')
		s2=s2+1
		print(s1)
		print(s2)
	elif(a=='s' and s=='p'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='r' and s=='s'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='r' and s=='p'):
		print('try')
		s2=s2+1
		print(s1)
		print(s2)
