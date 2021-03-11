a = 160402
b = 190784
c = 100321
d = abs(a - c)# regardless of which number is bigger,we can always get a positive number.
e = abs(b - a)
print(bool(d > e))

X = False
Y = True
Z = (X and not Y) or (Y and not X)
print(Z)
W= X!= Y #it is of the same as 10
print(W)
