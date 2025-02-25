
for i in range(1, 100):
    temp = i
    while temp % 2 == 0:
        temp //= 2
    if(temp == 1):
        print(i)