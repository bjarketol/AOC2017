import numpy as np

goal = 361527

x = np.zeros([1001, 1001], dtype=np.int32)

dir_changer = {'E': 'N',
               'N': 'W',
               'W': 'S',
               'S': 'E'}

steps = np.array([np.repeat(i, 2) for i in np.arange(1, 100)]).ravel()
print(steps)
i, j = 500, 500

val = 1
x[i, j] = val
k = 0
l = 0
d = 'E'
n = steps[l]

while val < goal:

    if d == 'E': i += 1
    if d == 'W': i -= 1
    if d == 'N': j += 1
    if d == 'S': j -= 1

    val = np.sum(x[i-1:i+2, j-1:j+2])
    print(i, j, l, n,  val)
    
    x[i,j] = val

    k += 1

    if k == n:
        d = dir_changer[d]
        l += 1
        k = 0
        n = steps[l]




