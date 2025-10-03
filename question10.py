salary=int (input("enter a salary: "))
age=int (input("enter your age: "))
if(salary>=20000 or age<=25):
    loan=int (input("loan amount"))
    if(loan>=50000):
        print("Maximum loan amount is 50000")
    else:
        print("you are elligible for loan")

else:
    print("not eligible")
