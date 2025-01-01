
# write  a program to find the greatest of four number enterd by user.

a1 = int(input('give umber 1 :'))
a2 = int(input('give umber 2 :'))
a3 = int(input('give umber 3 :'))
a4 = int(input('give umber 4 :'))

if(a1>a2 and a1>a3 and a1>a4):
    print(f'{a1}nuber is getert')
elif(a2>a1 and a2>a3 and a3>a4):
    print(f'{a2}nuber is getert')
elif(a3>a2 and a3>a1 and a3>a4):
    print(f'{a3}nuber is getert')
else:
    print(f'{a4}nuber is getert')
 
