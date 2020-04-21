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

name = input('enter the name: ')
text = f"Hello {name},\n Thank you for purchasing Herbalife products. I hope you are happy with Herbalife products.\n For your future Herbalife product purchases, I recommend you to use this site. It is Herbalife's site for me, as a distributor.\n You can buy there with %25 off with the code 25OFF25 \n You will just enter your email and create a password, and you are ready to go. You can use Paypal.
\n\n https://koca.goherbalife.com/en-us \n\n Thank you \n Koca"
print(text)