n = int(input('Enter a number: '))
prime_nums = []
for i in range(2, n):
    c = 0
    for ii in range(2, i):
        if i % ii == 0:
            c += 1
    if c == 0:
        prime_nums.append(i)

print(prime_nums)

