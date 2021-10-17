#  Morning Problem 2
#  average_height.py
#  1616898


# the floor() function might be useful
# for a floating point number x, floor(x) is the greatest integer <= x
import math #(I changed this because the original wasn't seeming to work...???)

# read in the input
numbers = list(map(int, input().split()))

# now "numbers" is a list containing all integers in the input
# solve the problem
#Find the sum of all numbers in list then divide by the number of input numbers
sum=0
for i in range(len(numbers)):
	sum=sum+(numbers[i])

#Divide by number of input numbers
average=sum/len(numbers)

#Round average down to nearest integer
average=math.floor(average)

# output the solution
print(average)
