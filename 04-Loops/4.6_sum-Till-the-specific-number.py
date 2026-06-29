"""Task 6
Take a number n from the user and print:
1
2
3
...
n"""
# Task 7 Take a number and calculate the sum of numbers from 1 to n.

number=int(input("Enter number n :"))

sum=0

for i in range (1 , number+1):
    print(i)
    sum+=i

print("Sum is :" , sum)