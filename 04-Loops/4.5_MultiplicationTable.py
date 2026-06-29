# Task 5:Print the multiplication table of 7.

for i in range(1,11):
    print("7 x ",i," = ",7*i)


#if the range is not known
table_number=int(input("Enter number for table: "))
start_number=int(input("Enter starting multiplication number for table: "))
end_number=int(input("Enter ending multiplication number for table: "))

count=start_number
for i in range (start_number , end_number+1):
    print(table_number ," x ",i," = ",table_number*i)