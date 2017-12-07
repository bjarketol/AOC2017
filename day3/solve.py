from collections import namedtuple
from math import fabs

goal = 361527

for ring in range(10000):

    corner_value = (ring*2 + 1)**2
    corner_coords = [ring, -ring]

    print(corner_value, corner_coords)

    if corner_value > goal:
        diff = corner_value - goal
        nside = 2 * corner_coords[0]
        div = diff // nside
        mod = diff % nside
     
        if div == 3:
            coords = [corner_coords[0], corner_coords[1] + nside - mod]
 
        break

steps = sum([int(fabs(c)) for c in coords])
print(steps)


import numpy as np

x = np.zeros([1001, 1001], dtype=np.int32)

i, j = 500, 500

dirMap = {'E': 'N', 'N':'W', 'W':'S', 'S':'E'}

x[i, j] = 1

step = 1
d = 'N'

i += step
x[i, j] = np.sum(x[i-1:i+1, j-1:j+1])

steps = [i,

k = 0
while True:

    if k % 2 == 0:
        step += 1
        
    if d == 'E':
        i += 1
    if d == 'N':
        j += 1
    if d == 'W':
        i -= 1
    if d == 'S':
        j -= 1

    x[i, j] = np.sum(x[i-1:i+1, j-1:j+1])

    d = dirMap[d]
    k += 1
        
    print(x)    












