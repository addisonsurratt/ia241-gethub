'''
lab 5
if, else, elif statement
'''

#3.1
alien_color='red'
if alien_color=='green':
    print('you got 5 points')

#3.2
if alien_color=='green':
    print('you got 5 points')
else:
    print('you got 10 points')
    
#3.3
favorite_fruits = ['banana','strawberry','pineapple']
print(favorite_fruits)
    
if 'pineapple' in favorite_fruits:
    print('you really like pineapple')
if 'strawberry' in favorite_fruits:
    print('you really like strawberry')
if 'banana' in favorite_fruits:
    print('you really like banana')
    
#3.4
age=21
if age<10:
    print('this person is a kid')
elif age<20:
    print('this person is a teenager')
else:
    print('this person is an adult')
    if age>65:
        print('this person is an elder')
