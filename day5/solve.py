
with open('input.txt', 'r') as f:
    offsets = [int(v.strip()) for v in f.readlines()]

part = 2
n = len(offsets)
i = 0
count = 0
while True:
    
    if ((i < 0) or (i >= n)):
        print('Jumped outside in %s jumps!' % count)
        break

    jump = offsets[i]
    
    if ((part == 2) and (jump >= 3)):
        offsets[i] -= 1
    else:
        offsets[i] += 1

    i += jump
    count += 1




