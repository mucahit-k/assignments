year = int(input('Enter a year to check if it is a leap year: '))

if year % 100 and year % 4 == 0 or year % 400 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year') 