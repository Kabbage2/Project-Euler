y = 0
x = 2520
while(True):

    for i in range(10, 20):
        
        if x % i == 0:
            y += 1
    if y == 10:
        print(x)
        break
    else:
        print(x)
        y = 0
        x += 2520