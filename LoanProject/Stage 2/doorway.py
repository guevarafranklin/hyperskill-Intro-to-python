a = int(input())
b = int(input())
c = int(input())

#door metrics
x = int(input())
y = int(input())

#if the size of the doorway is greater than or equal to any two dimensions of the box, it is considered that the box can be carried

if a <= x and b <= y:
    print("The box can be carried")
elif b <= x and b <= y:
    print("The box can be carried")
elif c <= x and c <= y:
    print("The box can be carried")
else:
    print("The box cannot be carried")
