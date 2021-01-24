import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style





style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)





def animate(i):
    graph_data = [    [1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4],
[1,5],
[2,3],
[3,4],
[4,7],
[5,4],
[6,3],
[7,5],
[8,7],
[9,4],
[10,4]]

    xs = []
    ys = []
    for line in graph_data:
        if len(line) > 1:
            x, y = line[0], line[1]
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)



ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

