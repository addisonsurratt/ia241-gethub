'''
lec 6
for loop
range function
'''
#for num in [1,2,3]:
#for word in 'this is lec6'.split():
 #   print(word)
   # for c in word:
    #  print(c)
    
 #   for num in [1,2,3]:
      #  if num>1:
      #      print(num)
            
#for i in range(1,5):
   # print(i)

num_list=[123,321,234,245,334]

possible_max_num = num_list[0]

for num in num_list:
    if num > possible_max_num:
        possible_max_num = num
print(possible_max_num)

