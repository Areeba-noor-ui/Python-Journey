# Create a function is_even(number) that prints:

number=int(input("Enter a number: "))

def isEven(number):
    if(number%2==0):
        print("Even")
    else:
        print("Odd")

isEven(number)
