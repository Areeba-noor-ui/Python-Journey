# Task 4:Print all odd numbers from 1 to 50.

for i in range (1,50,2):        
    print(i)

print("Second method Output:")

for i in range(1,51):
    if(i%2!=0):
        print(i)
    else:
        continue