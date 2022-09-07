binary_input = input('Binary: ')
reverse = binary_input[::-1]
summation = []
l = []
n = 1
i = 0
while i < len(reverse):
    l.append(n)
    n *= 2
    i += 1

z = list(zip(reverse, l))

for i in z:
    for j in i:
        if j == '1':
            summation.append(i[1])

print(sum(summation))
