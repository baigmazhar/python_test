'''
n=int(input("Enter an integer: "))
if(n % 2 ==0):
    print(n,"is a even number")
else:
    print(n,"is a odd number")
'''

a=100
b=34
c=89

# maximum number
if(a>b) and (a>c):
    print(a,"is greater number")
elif(b>a) and (b>c):
    print(b,"is greater number")
elif(c>a) and (c>b):
    print(c,"is greater number")

# minimum number
if(a<b) and (a<c):
    print(a,"is lower number")
elif(b<a) and (b<c):
    print(b,"is lower number")
elif(c<a) and (c<b):
    print(c,"is lower number")