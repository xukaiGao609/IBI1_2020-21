a = 1
b = 1
print(a)
print(b) # to make sure that the outcome contains the first two values of Fibonacci
for i in range(1,12):# make sure to get 13 values
    c = a + b # get the value, prepare for the next round
    a = b
    b = c
    print(c) # show the target value we get
