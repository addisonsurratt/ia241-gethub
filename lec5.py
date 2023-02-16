# import this
# print (1+15+
#            4564)
            
# 1 + 2 + \
# 12+456
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(id([1,2,3]))

print ( a == b)

print(a is b)

a = None

print(id(a))
print(id(None))

print(a is None)
print(a == None)

x =[]
print(x is None)

print( True and False)

if 2<1:
    print("2>1")
    print('another 2>1')
    if 3>1:
        print('3>1')
else:
    print('else statement')
        
print('out of it block')