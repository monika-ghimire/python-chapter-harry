# its a function which call itsself

'''
factorisal(1) = 1
factorisal(2) = 2x 1
factorisal(3) = 3 x 2 x1
factorisal(4) = 4 x 3x 2 x1
factorisal(5) = 5 x4 x 3x 2 x1

factorisal(n) = n x n -1 x.......3 x 2x 1


factorisal(n) = n * factorisal(n-1)
'''

def factorisal(n): 
    if(n==1 or n==0):
        return 1
    return n*factorisal(n-1)

n = int(input('enter a nuber :'))
print(f" numver factorisal is :{factorisal(n)} " , )
