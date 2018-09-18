#comparing 3 no.s
a=int(input("enter the first no."))
b=int(input("enter the second no."))
c=int(input("enter the third no."))
if(a>b & a>c):
    print("a=",a,"is greater")
elif(b>c):
    print("b=",b,"is greater")
else:
	print("c=",c,"is greater")