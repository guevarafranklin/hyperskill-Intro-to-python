def convert_temp (f):
    c = (f - 32) * 5 / 9
    return round(c, 3)

faren = int(input())
print(convert_temp(faren))