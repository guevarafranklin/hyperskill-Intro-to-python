a = int(input())
b = int(input())
h = int(input())

if h >= a and h <= b:
    print("Normal")
if h < a and h < b:
    print("Deficiency")
if h > a and h > b:
    print("Excess")