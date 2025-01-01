# a spam comment is defined as a text containg following keywords:
# "make a lot of money" , "buy now", " subsctibe this" , " click this", 
# write a programe to detect these spams


p1="make a lot of money" 
p2="buy now"
p3="subsctibe this" 
p4="click this"

mgs = input('enter your commnet :')

if(p1 in mgs or p2 in mgs or p3 in mgs or p4 in mgs):
    print('its a spam')
else:
    print('no worries')

