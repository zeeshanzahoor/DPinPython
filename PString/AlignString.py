for x in range(1,10):
    lj = "*".ljust(x,'*')
    print(lj)
for x in range(1,10):
    rj = ("*"*x).rjust(10,' ')
    print(rj)
for x in range(1,10,2):
    cj = ("*"*x).center(10,' ')
    print(cj)

    
c= "*"
for x in range(1,21,2):
    print((c*x).center(21)*5)
for x in range(21,0,-2):
    print((c*x).center(21)*5)

