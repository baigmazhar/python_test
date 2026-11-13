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
else:
    print(c,"is greater number")

# minimum number
if(a<b) and (a<c):
    print(a,"is lower number")
elif(b<a) and (b<c):
    print(b,"is lower number")
else:
    print(c,"is lower number")


'''
for loop tracing
for i in range(1,10):
    print(i)
    
    #loop area
    
#out of loop area

how actually tracing is happening
start for i in range(1,10):--->     print(i)-1     #first iteration
                                    print(i)-2      #second iteration
                                    print(i)-3      #third iteration
                                    print(i)-4      #fourth iteration
                                    print(i)-5      #fifth iteration
                                    print(i)-6      #sixth iteration
                                    print(i)-7      #seventh iteration
                                    print(i)-8      #eight iteration
                                    print(i)-9      #ninth iteration
loop exit because it goes till n-1
'''


for i in range(1,10):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")


total = 0
for i in range(1,5):
    total = total + i
    print(total)


#prime number
for i in range(1,8):
    if i%2==1:
        print(i,"prime number")
    else:
        print(i,"not prime number")

'''
#infinite loop
x=1
while x!=0:
    print(x)
    x=x+
'''

# for loop
n=10
sum=0
for i in range(1,n+1):    sum=sum+i
print(sum)

# while loop
n=10
i=1
sum=0
while i<n+1:
    sum=sum+i
    i=i+1
print(sum)

