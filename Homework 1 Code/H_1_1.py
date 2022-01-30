#Homework 1 Problem 1 Michael Bartlett

#Find the maximum of three numbers

def find_maximum(x, y, z):
    '''
    :param x: The first number to compare
    :param y: The second number to compare
    :param z: The third number to compare
    :return: The largest of the three numbers
    '''
    if(x > y):
        if(x > z):
            #If
            return x
        else:
            return z
    elif(y > z):
        return y
    else:
        return z

if __name__ == '__main__':
    print(find_maximum(1,2,3))
    print(find_maximum(3,2,1))
    print(find_maximum(1, 3, 2))