fibonacci = [1, 1]
while fibonacci[-1] < 55:
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)