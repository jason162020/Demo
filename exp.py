

def rome(w):

     y = []
     g= w
     a = list(g)
     x = len(a)

     for i in range(0, x):

         y.append(a[x-1-i])


     if y == a:
            print("true")
     else:
            print('false')

z=input('Enter a string ')
#Palindrome.rome(z)

#print(list(z))
#a=list(z)
#print(len(z))
rome(z)


s=[2,3,4,5,6,7,3]
