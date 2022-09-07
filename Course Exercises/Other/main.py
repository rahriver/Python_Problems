import plotext
import numpy as np

# x = np.random.random(100)
# y = np.random.random(100)

# plotext.scatter(x,y)
# plotext.title("Random Data Points")
# plotext.show()


x = np.arange(0,10,0.1)
y = np.sin(x)
plotext.plot(x, y, label="sin(x)", marker="dot", color="blue")
plotext.title("sin(x)")
plotext.show()

# l = 1000
# x = range(1, l+1)
# frames = 50
# plotext.title("Animation")
# plotext.clc()

# for i in range(frames):
#     plotext.clt()
#     plotext.cld()

#     y = plotext.sin(1, 4, l, 2 * i / frames)
#     plotext.xlim(0,400)
#     plotext.plot(x,y, marker="dot", color="red")
#     plotext.sleep(0.01)
#     plotext.show()

# days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# hours = [10,5,4,3,1,5,6]

# plotext.title("Study Hours")
# plotext.bar(days,hours)
# plotext.show()
