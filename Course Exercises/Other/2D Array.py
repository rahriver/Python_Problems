# Iterate through the 2D array and sum them up!
sum = 9
arr = [1,3,5,6,11,23]
d = []

for x in arr:
    if d == []:
        for y in arr:
            if x + y == 9:
                d.extend([x,y])
                break

print(d)
