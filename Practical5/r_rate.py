r = 1.2
n = 84
i = 1 # set an value to count the rounds
p = False
while p==False:
    p = True
    i = i+1 
    n = n*r + n
    if i < 6:  #make sure it goes 5 rounds
        p = False


print(n)
