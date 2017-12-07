
def is_valid_1(l):
    list_ = l.split()
    ntotal = len(list_)
    nfilter = len(set(list_))
    return True if ntotal == nfilter else False

def is_valid_2(l):
    sorted_ = [''.join(sorted(l)) for l in l.split()]
    ntotal = len(sorted_)
    nfilter = len(set(sorted_))
    return True if ntotal == nfilter else False


data = []
with open('input.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

sum_1 = 0
sum_2 = 0
for line in data:
    if is_valid_1(line):
        sum_1 += 1
    if is_valid_2(line):
        sum_2 += 1

print(sum_1, sum_2)


