# CONDITIONAL STATEMENTS
x= 10
if x>0:
    print("x ix positive")
if x<0:
    print("x ix negative")
if x==0:
    print("x ix zero")

odd or even
x=(int(input("Given number=")))
if x % 2 ==0:
    print("even")
if x % 2 !=0:
    print("odd")

a=(input("enter a number="))
b=(input("enter a number="))
c=(input("enter a number="))
if a>b and a>c:
    print ("a is greater than all")
if b>a and b>c:
    print ("b is greater than all")
if c>a and c>b:
    print ("c is greater than all")

a=int(input("enter a number="))
if a % 2 == 0:
    print ("even")
else:
    print ("odd")

a= (int(input("enter your age=")))
if a > 18:
    print ("eligible to vote")
else:
    print(" not eligible to vote")

# if elif else
a=(int(input("enter a number=")))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")

marks=(int(input("enter your marks=")))
if marks >0:
    if marks > 90 and marks <= 100:
        print("a grade")
    elif marks > 70 and marks <= 90:
        print("b grade")
    elif marks > 50 and marks <= 70:
        print("c grade")
    elif marks > 35 and marks <= 50:
        print("d grade")
    else:
        print("u failed")
else:
    print("invalid marks")


a=int(input("enter a number="))
if a>0:
    if a%2==0:
        print("even")
    else:
        print("odd")
else:
    print("invalid number")
     