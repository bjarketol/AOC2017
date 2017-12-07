
with open('input.txt', 'r') as f:
    string = f.read().strip()

digits = list(int(s) for s in string)

sum_ = 0

for i in range(len(digits)):
    
    print(i, (i+len(digits)//2) % len(digits))
    if digits[i] == digits[(i+len(digits)//2) % len(digits)]:
        sum_ += digits[i]
        
print(sum_)

