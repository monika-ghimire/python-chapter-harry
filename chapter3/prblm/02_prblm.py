# write a program to fill in letter template given below with name and data 

letter = """
    dear name 
    you are selected!
    date
"""
username = input('enter your name')
# print(letter)
print(letter.replace('name' , username).replace('date' , '2003 jan 8'))