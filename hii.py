

def hiii(s,num):
    x=''
    for i in range(0,num):
        x=s+x

    print(x)

def st(s):
    c=''
    for i in s:
       c=c+i*2
    print(c)








#x=int(input('enter number of print '))

#hiii('hi',x)
#print('hello'*7)
#f=input('enter a string ')
#st(f)

def prg(l):
    c=0
    p=len(l)
    y=0
    for i in range(0,p):

        if l[i]!=13  :
            c=c+l[i]

        else:
            c=c-l[i+1]



    print(c)

def second_large(z):
    l=0
    s=0
    for i in z:
        if i>=l:
            s=l
            l=i
        elif i>=s:
            s=i
        else:
            pass
    print('second larger value ',s)


x=int(input('enter array size' ))
y=[]
for i in range(0,x):
    y.append(int(input("enter next value ")))
#prg(y)
print(y)
second_large(y)