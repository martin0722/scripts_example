import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import copy

A = np.random.rand(200)

fig = plt.figure()
rects = plt.bar(np.arange(len(A)) + 1, A)

rs = [r for r in rects]

def bobble_sort(array):
    for ii in range(len(array) - 1):
        if array[ii] > array[ii + 1]:
            array[ii], array[ii + 1] = array[ii + 1], array[ii]


def init():
    return rs 

bucket_size = 1
group = None
def animate(i):
    global group, A
    if group is None:
        group = []
        for i in range(bucket_size):
            group.append([])
        maxV = copy.copy(A[0])
        minV = copy.copy(A[0])
        for a in A:
            if a > maxV:
                maxV = copy.copy(a)
            if a < minV:
                minV = copy.copy(a)
        step = (maxV - minV) / float(bucket_size)
        for a in A:
            bucket = np.floor((a - minV) / step)
            bucket = np.minimum(bucket, bucket_size - 1)
            group[int(bucket)].append(a)
    else:
        A = []
        for g in group:
            bobble_sort(g)
            A += g

    for a, r in zip(A, rs):
        r.set_height(a)
    return rs 

ani = animation.FuncAnimation(fig=fig, func=animate,
    frames=100, init_func=init, interval=1, blit=False)
plt.show()
