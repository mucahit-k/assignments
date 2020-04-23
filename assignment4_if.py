num = int(input('Enter a number to check if it is a prime number: '))

x = 0
for i in range(2, num):
    if num % i == 0:
        x += 1
if x == 0:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
