# n = int(input())

# #Creating while loop while n <= 1
# counter = n
# while counter > 1:
#     counter -= 1
#     n *= counter    
# print(n)


print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
number = int(input())

counter = 0
while counter <= number:
    print(str(counter) + "!")
    counter += 1

print('Completed, have a nice day!')
