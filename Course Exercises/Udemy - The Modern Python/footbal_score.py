l = []
try:
    while len(l) < 30:
        user = int(input('num:'))
        l.append(user)
except ValueError:
    print('Give me number!')

win = [x for x in l if x == 3]
draw = [x for x in l if x == 1]
loss = [x for x in l if x == 0]

print(f"{sum(l)} Draws: {len(draw)} Losses: {len(loss)} Wins: {len(win)}")
