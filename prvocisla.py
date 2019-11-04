num = int(input('Zadaj číslo:'))
for i in range(2, num + 1):
    if(num % i == 0):
        prvocislo = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                prvocislo = 0
                break
            
        if (prvocislo == 1):
            print(i)