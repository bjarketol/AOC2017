import numpy as np

data = np.genfromtxt('input.txt', dtype=np.int32)

ncol, nrow = data.shape

sum_ = 0
vals = []
for irow in range(nrow):
    
    row = data[irow,:]
    
    for val1 in row:
        for val2 in row:
            
            if val1 == val2:
                continue

            if val2 % val1 == 0:
                vals.append(val2 // val1)

            
    sum_ += (np.max(row) - np.min(row))

print(sum_)
print(sum(vals)) 



