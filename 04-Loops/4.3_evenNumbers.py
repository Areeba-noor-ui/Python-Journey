# Task 3: Print all even numbers from 1 to 50.

for i in range (2,51,2):        #range(start,stop,step)
    print(i)

#other method

print("Second method Output:")

for i in range(1,51):
    if(i%2==0):
        print(i)
    else:
        continue