import operator

with open('input.txt', 'r') as f:
    banks = [int(v) for v in f.read().strip().split()]

states = []
size = len(banks)
count = 0
while True:
    
    i, n = max(enumerate(banks), key=operator.itemgetter(1))

    banks[i] = 0
    for _ in range(n):
        i += 1
        if i >= size:
            i -= size
        banks[i] += 1
    
    count += 1

    if banks in states:
        print('Duplicate in %s tries!' % count)
        
        irepeat = states.index(banks)
        print(irepeat)
        print(count - irepeat - 1)


        break
    else:
        states.append(banks.copy())



