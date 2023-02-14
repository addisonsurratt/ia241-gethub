'''
lab 4
dict and tuple
'''

my_tuple = 'a','b','c','d','e'

print(my_tuple[0:2])

my_car={
        'color':'red',
        'maker':'toyota',
        'year':2015
            }
print(my_car.get('color'))
my_car['model']='venza'
print(my_car)
my_car['year']=2020
print(my_car)

print(len(my_car))
print('red'in my_car.values())
