# The Python map() function applies a specific operation to every item in an iterable (like a list) without using a manual for loop.

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

letters= ['a','b','c','d'];
capital_letters=map(str.upper,letters)
print (list (capital_letters) )

numbers = [1, 2, 3, 4, 5];
numbers= map (lambda x:x*x ,numbers)
print (list(numbers))