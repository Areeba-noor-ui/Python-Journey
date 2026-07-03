# Task 

# Search for a number.

numbers=[23,67,89,32,14,56]

target=int(input("Enter Number to find:\n"))

found=False

for index,value in enumerate(numbers):
    if (target==value):
        print("Target ",value ," found at index ",index )
        found=True
        break

if  not found:
    print("Target value not found.")
        
