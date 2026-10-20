# calculate a sutudents grade from marks

user_input=int(input("enter a marks:"))

if user_input <40:
    print("D+")

elif user_input >=40 and user_input <60:
    print("C+")


elif user_input >=60 and user_input <70:
    print("B+")

else:
    print("A+")