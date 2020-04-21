num_1 = input('Enter a number to check if it is an Armstrong number: ')

if ',' in num_1 or '.' in num_1:
    print('Please enter an integer number')
elif num_1[0] == '-':
    print('Please enter a positive number')
elif not num_1.isdigit():
    print('Do not use any entries other than numeric values')
else:
    num_2 = list(num_1)
    num_list = [int(i)**len(num_2) for i in num_2]
    if sum(num_list) == int(num_1):
        print(f'{num_1} is an Armstrong number')
    else:
        print(f'{num_1} is not an Armstrong number')
