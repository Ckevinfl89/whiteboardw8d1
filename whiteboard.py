# The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.

# Examples:
# a = "I like turtles"
# b = "I like turkeys"
# Result: 3

# a = "Hello World"
# b = "Hello World"
# Result: 0

# a = "espresso"
# b = "Expresso"
# Result: 2

# Notes:
# You can assume that the two inputs are ASCII strings of equal length.


def solution(a, b):
   
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
            
    return distance


def hamming2(s1,s2):
    return sum(map(lambda tup:tup[0]!=tup[1],zip(s1,s2)))