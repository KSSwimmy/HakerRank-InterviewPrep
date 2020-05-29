# def rotLeft(n, d):
#     return a[d:]+ a[:d]

# print(5,4)

#Given: 2 paramaters. a number of intergers in the array (a = 5) , the number of rotations (d = 4) 
#Find: an array of intergers a [1,2,3,4,5] and preforms 4 rotations
#Return: the new rotated array 

array = [1,2,3,4,5]

d_value = 4

def rotate(a,d):
    #a is the array (list in Python)
    #d is the number of times it will rotate
    #we can the slice list to return the asked input. 
    return a[d:]+ a[:d]

print(rotate(array, d_value))