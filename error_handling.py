grade1=input("enter the first grade!")
grade2=input("enter the second grade!")
try:
    grade1=int(grade1)
    grade2=int(grade2)
    print("the first grade is", grade1)
    print("the second grade is", grade2)
except:
    print("invalid grade")
