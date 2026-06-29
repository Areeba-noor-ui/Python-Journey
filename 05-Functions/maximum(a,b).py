# task 3:Create a function maximum(a, b) that prints the larger number.

number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))

def maximum(a,b):
    if(a>b):
        print("first Number " , a ," is greater than " , b)
    elif(a<b):
        print("Second Number " , b ," is greater than " , a)
    else:
        print("Both are equal")

maximum(number1,number2)
        