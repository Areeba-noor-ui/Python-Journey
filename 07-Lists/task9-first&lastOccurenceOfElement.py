# Find the first occurrence of a number.

# Find the last occurrence of a number.


numbers=[1,5,6,7,4,3,2,2,1,5,5,1,6]

target=int(input("Enter target Number:\n"))

found=False

count=0

for i in range(len(numbers)):
    
    if(numbers[i]==target):
        found=True
        print("number first ocurrence is at index : ",i)
        break

last_occurrence = -1

for i in range(len(numbers)):

    if numbers[i] == target:
        last_occurrence = i

if last_occurrence != -1:
    print("number first ocurrence is at index : ",last_occurrence)


if  not found:
    print("Target value not found.")
        
      