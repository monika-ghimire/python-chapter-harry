# write a program to find whether a fiven username contains less then 10 character or not

name = input('enter you name to check :')

if len(name)== 10:
    print('equal to 10 char:' ,len(name))
elif len(name) > 10:
    print('geather then 10 char:' ,len(name) )
else:
    print('less then 10 char:' , len(name))