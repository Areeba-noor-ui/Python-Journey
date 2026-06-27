marks=int(input("Enter Marks out of 100 = "))

if (marks>100):
    print("Enter Correct marks")

elif (marks>=90):
    print("Grade : A")

elif (marks>=80 and marks<90):
    print("Grade : B")

elif (marks>=70 and marks<80):
    print("Grade : C")

elif (marks>=60 and marks<70):
    print("Grade : D")

else:
    print("Grade : F")