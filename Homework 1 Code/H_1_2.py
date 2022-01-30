#Homework 1 Problem 2 Michael Bartlett

#Find the sum of all integers plus 1 then squared from 1 to n
def sum_i_plus_1_squared(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i + 1) ** 2
    return sum

if __name__ == '__main__':
    print(sum_i_plus_1_squared(1))
    print(sum_i_plus_1_squared(2))
    print(sum_i_plus_1_squared(5))
