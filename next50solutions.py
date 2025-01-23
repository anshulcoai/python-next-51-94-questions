# 51.Determine the type of triangle based on sides (equilateral, isosceles, scalene).
'''
a=int(input("Enter the First side of Triangle :"))
b=int(input("Enter the Second side of Triangle :"))
c=int(input("Enter the Third side of Triangle :"))
print("First side is :",a)
print("Second side is :",b)
print("Third side is :",c)
if a==b and b==c and c==a:
    print("Triangle is an equilateral")
elif a==b or b==c or c==a:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
'''

# 52.Determine the type of triangle based on angles (acute, obtuse, right).
'''
a=int(input("Enter First Angle :"))
b=int(input("Enter Second Angle :"))
c=int(input("Enter Third Angle :"))
if a<90 and b<90 and c<90:
    print("This is an Acute Triangle")
elif a>90 and b<90 and c<90 or a<90 and b>90 and c<90 or a<90 and b<90 and c>90:
    print("This is an obtuse Triangle")
elif a==90 and b<90 and c<90 or a<90 and b==90 and c<90 or a<90 and b<90 and c==90:
    print("This is right angle Triangle")
else:
    print("Invalid Triangle")
'''

# 53.Calculate the grade based on marks (A, B, C, D, F).
'''
a=int(input("Enter your marks :"))

if a>90 and a<100:
    print("A grade")
elif a>80 and a<90:
    print("B grade")
elif a>70 and a<80:
    print("C grade")
elif a>60 and a<70:
    print("D grade")
elif a>50 and a<60:
    print("E Grade")
elif a<50:
    print("Fail")
else:
    print("Invalid numbers")
'''

# 54.Determine the day of the week based on a number (1-7)
'''
a=int(input("Enter a week number :"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thurday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Invalid week number")
'''

# 55.Check if a number is a multiple of 4.
'''
a=int(input("Enter a number :"))
print(a)
if a%4==0:
    print("Number is a multiple of 4")
else:
    print("Number is not a multiple of 4")
'''

# 56.Check if a number is a multiple of 6.
'''
a=int(input("Enter a number :"))
print(a)
if a%6==0:
    print(a,"is a multiple of 6")
else:
    print(a,"is not a multiple of 6")
'''

# 57. Check if a number is a multiple of 8.
'''
a=int(input("Enter a number :"))
print(a)
if a%8==0:
    print(a,"is the multiple of 8")
else:
    print(a,"is not the multiple of 8")
'''

# 58.Determine if a character is a special symbol.
'''
ch=input("Enter a character :")
print(ch)
if ch>='0' and ch<='9':
    print("This is a number")
elif ch>'a'and ch<'z':
    print("This is an alphabet")
else:
    print("This is a special symbol")
'''    

# 59.Check if a number is positive, negative, or zero
'''
a=int(input("Enter a number :"))
print(a)
if a>0:
    print("Number is positive")
elif a<0:
    print("Number is negative")
elif a==0:
    print("Number is Zero")
'''

# 60.Check if the difference between two numbers is positive.
'''
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=a-b
print(c)
if c>0:
    print("Number is positive")
elif c==0:
    print("Number is Zero")
else:
    print("Number is negative")
'''

# 61.Check if the difference between two numbers is negative.
'''
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=a-b
print(c)
if c>0:
    print("Number is positive")
elif c==0:
    print("Number is Zero")
else:
    print("Number is negative")
'''

# 62.Check if the difference between two numbers is zero.
'''
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=a-b
print(c)
if c>0:
    print("Number is positive")
elif c==0:
    print("Number is Zero")
else:
    print("Number is negative")
'''

# 63.Determine the larger of two numbers using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
if a>b:
    print(a," is greater")
else:
    print(b,"is greater")
'''

# 64. Determine the smaller of two numbers using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
if a<b:
    print(a," is smaller")
else:
    print(b,"is smaller")
'''

# 65.Find the largest of three numbers using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
'''

# 66.Find the smallest of three numbers using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))
if a<b and a<c:
    print(a,"is smaller")
elif b<a and b<c:
    print(b,"is smaller")
else:
    print(c,"is smaller")
'''

# 67.Check if a character is uppercase using a ternary operator.
'''
a=input("Enter a character :")
if a>'A' and a<'Z':
    print("It is an uppercase ")
else:
    print("It is not an uppercase")
'''

# 68.Check if a character is lowercase using a ternary operator.
'''
a=input("Enter a character :")
if a>'a' and a<'z':
    print("It is lowercase")
else:
    print("It is not lowercase")
'''

# 69. Check if a character is a digit using a ternary operator.
'''
a=int(input("Enter a character :"))
if a>0 or a<0:
    print("Its a digit")
else:
    print("Its not a digit")
'''    

# 70.Determine if a number is even using a ternary operator.
'''
a=int(input("Enter a number :"))
if a%2==0:
    print("Number is Even")
else:
    print("Number is not even")
'''

# 71.Determine if a number is odd using a ternary operator.
'''
a=int(input("Enter a number :"))
if a%2!=0:
    print("Number is odd")
else:
    print("Number is not odd")
'''

# 72.Check if the sum of two numbers is even using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=a+b
print(c)
if c%2==0:
    print("Number is even")
else:
    print("Number is not even")
'''

# 73.Check if the sum of two numbers is odd using a ternary operator.
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=a+b
print(c)
if c%2!=0:
    print("Number is odd")
else:
    print("Number is not odd")
'''

# 74.Check if a year is a leap year using a ternary operator.
'''
a=int(input("Enter a Year :"))
print(a)
if a%4==0:
    print(a,"is Leap year")
else:
    print(a,"is not a leap year")
'''

# 75.Determine the quadrant of a point (x, y) in the Cartesian plane.
'''
x=int(input("Enter a value of x :"))
y=int(input("Enter a value of y :"))

if x>0 and y>0:
    print("It is the first quadrant")
elif x<0 and y>0:
    print("It is the second quadrant")
elif x<0 and y<0:
    print("It is the Third quadrant")
else:
    print("It is fourth quadrant")
'''

#76. Check if a number is divisible by 5 using a ternary operator.
'''
a=int(input("Enter a number :"))
if a%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")
'''

# 77. Check if a number is divisible by 11.
'''
a=int(input("Enter a number :"))
if a%11==0:
    print("Number is divisible by 11")
else:
    print("Number is not divisible by 11")
'''

#78.Check if a number is a perfect number.
'''
Already done
'''

#79.

#80.

#81. Determine if a person is eligible for a driving license(age >= 18).
'''
a=int(input("Enter your age :"))

if a>=18:
    print("You are eligible for Driving license")
else:
    print("you have to wait for",18-a,"years for your driving license")
'''

#82. Determine if a person is a child (age < 13).
'''
a=int(input("Enter your age :"))

if a<13:
    print("you are a child")
elif a>=18:
    print("you are an adult")
else:
    print("you are not child")
'''

#83.Determine if a number is greater than another number.
'''
a=int(input("Enter First number :"))
b=int(input("Enter Second number :"))
if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)
'''

#84.Determine if a number is less than another number.
'''
Already Done
'''

#85.Check if a number is equal to another number.
'''
a=int(input("Enter first number :"))
b=int(input("Enter Second number :"))
if a==b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
'''

#86.Check if a number is not equal to another number.

#87.Determine if a number is positive.
'''
a=int(input("Enter a number :"))
if a>0:
    print("Number is positive")
elif a==0:
    print("Number is zero")
else:
    print("Number is negative")
'''

#88.Determine if a number is negative.
'''
Already Done
'''
#89.Determine if a number is zero.
'''
Already Done
'''

#90.Check if a character is an uppercase letter using nested
'''
a1=input("Enter a alphabet :")
if a1>='A' and a1<='Z':
    print("Its an Uppercase")
elif a1>='a' and a1<='z':
    print("Its a Lowercase")
else:
    print("Not an alphabet")
'''

#91.Determine if a person is an adult (age >= 18)
'''
a=int(input("Enter your age :"))
if a>=18:
    print("Person is an adult")
else:
    print("Person is not an adult")
'''

#92.Check if a number is within a specified range (x <= num <= y).
'''
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
num=int(input("Enter a number u want to check:"))
if num>a and num<b:
    print("Number is within a range")
else:
    print("Number is not within a range")
'''


#93.Determine if a number is positive, negative, or zero.
'''
a=int(input("Enter your number :"))
if a>0:
    print("Number is positive")
elif a<0:
    print("Number is negative")
elif a==0:
    print("Number is zero")
else:
    print("Invalid")
'''

#94.Check if the product of two numbers is positive.
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=a*b
print(c)
if c>0:
    print("Product is positive :")
else:
    print("product is not positive")









































































































































































    














