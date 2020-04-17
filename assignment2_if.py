age = input('Are you a cigarette addict older than 75 years old? ').lower()  
chronic = input('Do you have a severe chronic disease? ').lower()  
immune = input('Is your immune system too weak? ').lower()  
yes_list = ['yes', 'y', 'true']
if age in yes_list:
    print('You are at risk of death from coronavirus.')
else:
    if chronic in yes_list:
        print('You are at risk of death from coronavirus.')
    else:
        if immune in yes_list:
            print('You are at risk of death from coronavirus.')
        else:
            print('You are not at risk of death from coronavirus, even though you need to be careful about it.')

