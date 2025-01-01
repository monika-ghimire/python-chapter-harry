# write a program fint out wheter a student has passed or failed it
#  required as total of 40% and  
# at least 33% in each subjext to pas.
#  assume 3 student and take marks as an input from user. 

m1 = int(input('enter marks 1:'))
m2 = int(input('enter marks 2:'))
m3 = int(input('enter marks 3:'))

#check for total percenet
total_percentage = (100*(m1 + m2 + m3))/300

if (total_percentage >= 40 and m1 > 33 and m2 > 33 and m3 > 33):
    print("pass" , total_percentage )
else:
    print('fail' ,total_percentage)

