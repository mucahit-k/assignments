num_1 = input('Enter a positive number to check if it is an Armstrong number: ')
while True:
    
    if not num_1.isdigit():
        num_1 = input('Enter a positive number to check if it is an Armstrong number: ')
    else:
        num_2 = list(num_1)
        num_list = [int(i)**len(num_2) for i in num_2]
        if sum(num_list) == int(num_1):
            print(f'{num_1} is an Armstrong number')
        else:
            print(f'{num_1} is not an Armstrong number')
        break