x = 0
y = 1
z = 0
sum = 0

while z < 4000000:
    z = x + y
    x = y
    y = z 

    if z < 4000000 and z % 2 == 0:
        sum += z


print(sum)