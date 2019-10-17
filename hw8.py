
# List comprehension exercise II:
# Use a list comprehension to make a list containing tuples (i, j) where i goes from 1 to 10 and j is corresponding i squared.

# l1 = list()
# for i in range(1,10):
# 	l1.append((i, i*i))	
# print(l1)

# List comprehension exercise I:
# Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Now, make a program (no longer than one line) that makes a new list containing all the values in a but no even numbers. 

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in a:
# 	if i % 2:
# 		print(i)




# Dict comprehension exercise:
# Make a program that given a whole sentence (a string) will make a dict containing all unique words as keys and the number of occurrences as values.

# d1 = dict()
# str1 = 'I love Python Python Python love'
# str2 = list()
# str2 = str1.split()
# print(str2)
# for s in str2:
# 	d1[s] = str2.count(s)
# print (d1)


# Factorial:
# To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example: 3! is equal to 123.

# num = int(input("Input your integer: "))
# factorial = 1
# for i in range(1,num+1):
# 	factorial *= i
# print(factorial)



# Digits sum:
# Write a program called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.

# number = input("Enter your integer: ")
# summ = 0
# for n in number:
# 	summ += int(n)
# print(summ)


# Remove duplicates:
# Write a program remove_duplicates that takes in a list and removes elements of the list that are the same.For example: remove_duplicates([1,1,2,2]) should return [1,2].

# numbers = [1,1,1,1,5,4,5,1]
# no_dup = []
# for ind, num in enumerate(numbers):
# 	if num not in no_dup:
# 		no_dup.append(num)
# print(no_dup)




# Count:
# Define a program called count that has two arguments called sequence and item. Return the number of times the item occurs in the list.For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

# s = 'I love Italy. Also, I love icecream'

# s = s.split()

# counter = 0
# word = 'I'
# print(s.count(word))





