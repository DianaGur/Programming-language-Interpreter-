# ----------------------------------------Question 1--------------------------------------------

# Question: Implement in a Python language, a factorial function in one line by using lambda expressions.

# Answer:   factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Example:
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


result = factorial(5)
print("Factorial of 5:", result)  # Output: 120


# ----------------------------------------Question 2--------------------------------------------

# Question: Write the shortest Python program, that accepts a list of strings and returns a single string
# that is a concatenation of all strings with a space between them. Do not use the "join" function.
# Use lambda expressions.

# Answer:   concat = lambda lst: reduce(lambda x, y: x + ' ' + y, lst)

# Example:
from functools import reduce


def concat_strings(last):
    return reduce(lambda x, y: x + ' ' + y, last)


strings = ["hello", "world", "how", "are", "you"]
print(concat_strings(strings))  # Output: hello world how are you


# ----------------------------------------Question 3--------------------------------------------

# Question: Write a Python function that takes a list of lists of numbers,
# and returns a new list containing the cumulative sum of squares of even numbers in each sublist.
# Use at least 5 nested lambda expressions in your solution.

# Answer:   from functools import reduce

# cumulative_sum_of_squares_of_even_numbers = lambda list_of_lists: [
# reduce(lambda x, y: x + y,  # Reduce to get the sum
# map(lambda num: num ** 2,  # Map to square each number
# filter(lambda num: num % 2 == 0, sublist)))  # Filter to select even numbers
# for sublist in list_of_lists]  # Iterate over each sublist

# Example:


def cumulative_sum_of_squares_of_even_numbers(list_of_lists1):
    return [
        reduce(
            lambda x, y: x + y,  # Reduce to get the sum
            map(
                lambda num: num ** 2,  # Map to square each number
                filter(
                    lambda num: num % 2 == 0, sublist  # Filter to select even numbers
                )
            )
        )
        for sublist in list_of_lists1  # Iterate over each sublist
    ]


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even_numbers(list_of_lists)
print(result)  # Output: [4, 52, 64]

# ----------------------------------------Question 4--------------------------------------------


# Question: Rewrite the following program in one line by using the nested filter, map and reduce functions:

# Answer: from functools import reduce
# sum_squared = reduce(lambda x, y: x + y,  # Reduce to get the sum
# map(lambda x: x**2,  # Map to square each number
# filter(lambda x: x % 2 == 0, nums)))  # Filter to select even numbers

# Example:
# ----------------------------------------Question 1--------------------------------------------

# Question: Implement in a Python language, a factorial function in one line by using lambda expressions.

# Answer:   factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Example:
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


result = factorial(5)
print("Factorial of 5:", result)  # Output: 120


# ----------------------------------------Question 2--------------------------------------------

# Question: Write the shortest Python program, that accepts a list of strings and returns a single string
# that is a concatenation of all strings with a space between them. Do not use the "join" function.
# Use lambda expressions.

# Answer:   concat = lambda lst: reduce(lambda x, y: x + ' ' + y, lst)

# Example:
from functools import reduce


def concat_strings(last):
    return reduce(lambda x, y: x + ' ' + y, last)


strings = ["hello", "world", "how", "are", "you"]
print(concat_strings(strings))  # Output: hello world how are you


# ----------------------------------------Question 3--------------------------------------------

# Question: Write a Python function that takes a list of lists of numbers,
# and returns a new list containing the cumulative sum of squares of even numbers in each sublist.
# Use at least 5 nested lambda expressions in your solution.

# Answer:   from functools import reduce

# cumulative_sum_of_squares_of_even_numbers = lambda list_of_lists: [
# reduce(lambda x, y: x + y,  # Reduce to get the sum
# map(lambda num: num ** 2,  # Map to square each number
# filter(lambda num: num % 2 == 0, sublist)))  # Filter to select even numbers
# for sublist in list_of_lists]  # Iterate over each sublist

# Example:


def cumulative_sum_of_squares_of_even_numbers(list_of_lists1):
    return [reduce(lambda x, y: x + y,  # Reduce to get the sum map(lambda num: num ** 2,  # Map to square each number
            filter(lambda num: num % 2 == 0, sublist))  # Filter to select even numbers
            for sublist in list_of_lists1]  # Iterate over each sublist


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even_numbers(list_of_lists)
print(result)  # Output: [4, 52, 128]


# ----------------------------------------Question 4--------------------------------------------


# Question: Rewrite the following program in one line by using the nested filter, map and reduce functions:

# Answer: from functools import reduce
# sum_squared = reduce(lambda x, y: x + y,  # Reduce to get the sum
# map(lambda x: x**2,  # Map to square each number
# filter(lambda x: x % 2 == 0, nums)))  # Filter to select even numbers

# Example: 
from functools import reduce

def sum_squared_even(nums1):
    return reduce(
        lambda x, y: x + y,  # Reduce to get the sum
        map(
            lambda x: x ** 2,  # Map to square each number
            filter(
                lambda x: x % 2 == 0, nums1  # Filter to select even numbers
            )
        )
    )


nums = [1, 2, 3, 4, 5, 6]
result = sum_squared_even(nums)
print(result)  # Output: 56


# ----------------------------------------Question 5--------------------------------------------

# Question: Write a one-line function that accepts as an input a list of lists containing strings
# and returns a new list containing the number of palindrome strings in each sublist.
# Use nested filter/map/reduce functions.

# Answer:  from functools import reduce
# count_palindromes = lambda list_of_lists: [
# reduce(lambda x, y: x + 1 if y == y[::-1] else x,  # Reduce to count palindromes
# filter(lambda x: isinstance(x, str), sublist),  # Filter to select strings
# 0)  # Initial value for counting
# for sublist in list_of_lists]  # Iterate over each sublist

# Example:
def count_palindromes(list_of_lists2):
    return [reduce(lambda x, y: x + 1 if y == y[::-1] else x,  # Reduce to count palindromes
                   filter(lambda x: isinstance(x, str), sublist),  # Filter to select strings
                   0)  # Initial value for counting
            for sublist in list_of_lists2]  # Iterate over each sublist


list_of_lists = [['racecar', 'hello', 'madam'], ['python', 'level', 'stats'], ['abc', 'deed', 'xyz']]
result = count_palindromes(list_of_lists)
print(result)  # Output: [2, 2, 1]from functools import reduce


# ----------------------------------------Question 6--------------------------------------------

# Question: Explain the term "lazy evaluation" in the context of the following program:

# Answer: The generate_values function is not explicitly called to completion. Instead, a list comprehension
# [square(x) for x in generate_values()] is used directly. This creates a generator expression, which
# Lazily generates values from the generate_values function as they are needed by the square function. As
# a result, the generate_values function is only called as many times as necessary to produce the required
# values for squaring. This demonstrates lazy evaluation, where computations are deferred until their
# results are required.

# In summary, lazy evaluation defers the evaluation of expressions until their results are needed,
# allowing for more efficient use of resources and potentially avoiding unnecessary computations. In
# the provided program, lazy evaluation is demonstrated by delaying the generation and processing of
# values until they are used in the list comprehension.


# ----------------------------------------Question 5--------------------------------------------

# Question: Write a one-line function that accepts as an input a list of lists containing strings
# and returns a new list containing the number of palindrome strings in each sublist.
# Use nested filter/map/reduce functions.

# Answer:  from functools import reduce
# count_palindromes = lambda list_of_lists: [
# reduce(lambda x, y: x + 1 if y == y[::-1] else x,  # Reduce to count palindromes
# filter(lambda x: isinstance(x, str), sublist),  # Filter to select strings
# 0)  # Initial value for counting
# for sublist in list_of_lists]  # Iterate over each sublist

# Example:
def count_palindromes(list_of_lists2):
    return [reduce(lambda x, y: x + 1 if y == y[::-1] else x,  # Reduce to count palindromes
                   filter(lambda x: isinstance(x, str), sublist),  # Filter to select strings
                   0)  # Initial value for counting
            for sublist in list_of_lists2]  # Iterate over each sublist


list_of_lists = [['racecar', 'hello', 'madam'], ['python', 'level', 'stats'], ['abc', 'deed', 'xyz']]
result = count_palindromes(list_of_lists)
print(result)  # Output: [2, 2, 1]from functools import reduce


# ----------------------------------------Question 6--------------------------------------------

# Question: Explain the term "lazy evaluation" in the context of the following program:

# Answer: The generate_values function is not explicitly called to completion. Instead, a list comprehension
# [square(x) for x in generate_values()] is used directly. This creates a generator expression, which
# Lazily generates values from the generate_values function as they are needed by the square function. As
# a result, the generate_values function is only called as many times as necessary to produce the required
# values for squaring. This demonstrates lazy evaluation, where computations are deferred until their
# results are required.

# In summary, lazy evaluation defers the evaluation of expressions until their results are needed,
# allowing for more efficient use of resources and potentially avoiding unnecessary computations. In
# the provided program, lazy evaluation is demonstrated by delaying the generation and processing of
# values until they are used in the list comprehension.
