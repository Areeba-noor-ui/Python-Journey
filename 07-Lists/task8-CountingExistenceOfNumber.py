# task-CountingExistenceOfNumber

numbers=[1,5,6,7,4,3,2,2,1,5,5,1,6,]

target=int(input("Enter target Number:\n"))

count=0

for i in range(len(numbers)):
    if(numbers[i]==target):
        count+=1

print("Number exists " , count," times")
      