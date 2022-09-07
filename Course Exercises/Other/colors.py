color = input('color: ').lower()
depth = int(input('depth: '))
colors = {
    'red':64.5,
    'orange':23.5,
    'yellow':3.9,
    'purple':1.13,
    'green':1.1,
    'blue':0.52
        }

def calc(color,depth):
    i = 1
    R = 100
    if color in colors:
        while i <= depth:
            R -= (colors[color]/100) * R
            i += 1
        print(f"{round(R,3)} % In {depth} Meter")
    else:
        raise ValueError('Color not found')

calc(color,depth)
