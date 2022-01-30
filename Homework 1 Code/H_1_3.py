#Homework 1 Problem 3 Michael Bartlett

#Print all the numbers from n to 0 decreasing in increaments of 0.5. Includes 0 as an output
def decreasing_printing(n):
    while(n >= 0):
        print(n)
        n -= 0.5

if __name__ == '__main__':
    decreasing_printing(3)
