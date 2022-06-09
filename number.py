import random

def createList(m,n):
    lst = []
    for i in range(m,n+1):
        lst.append(i)
    return(lst)

while 1:
    n = int(input("Enter range (Upper limit): "))
    m = int(input("Enter range (Lower limit): "))

    if m > n:
        print('Please try again.')
    else:
        break

while n < 50:
    n = int(input('Please enter again (above 50):'))

while m > 50:
    m = int(input('Please enter again (below 50):')) 

y = createList(m,n) 

while 1:
    x = random.choice(y)
    print(x)
    if x == 50:
        break
    

