x = 2000
count = 0 
for x in range(2001,2101,1):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print(x,end=' ')
        count += 1
        if count % 10 == 0:
            print()