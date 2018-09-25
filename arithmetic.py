def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def div(a,b):
	return a/b

i=int(input("enter value of a:"))
j=int(input("enter value of b:"))
o=input("what operation do you want?+,-,*,/->")

if(o=='+'):
    r=add(i,j)
elif(o=='-'):
 	r=sub(i,j)
elif(o=='*'):
 	r=mult(i,j)
elif(o=='/'):
 	r=div(i,j)
print(r)
