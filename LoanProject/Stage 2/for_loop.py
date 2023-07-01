n = int(input("Enter a number of iterations to try: "))
stored = []
for i in range(n):
    x = int(input("Enter the number to be divided by 7: "))
    if x % 7 == 0: 
            
        stored.append(x ** 2)

print(str(stored))