# # factorial
# def factorial(num):
#     fact=1
#     for i in range (1,num+1):
#         fact=fact*i
#     return fact

# num = int (input("Enter the number:"))
# result=factorial(num)

# print("Factorial:",result)


# Even or Odd
# def EvenOdd(num):
#     if num %2== 0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")

# num=int(input ("enter the number:"))
# EvenOdd(num)

# # maximun of three
# def maximum(a,b,c):
#     if a > b and a > c:
#         print(a,"is Maximum")
#     elif b > a and b > c:
#         print(b,"is Maximum")
#     else:
#         print(c,"is Maximum")

# a=int(input("Enter First Number:"))
# b=int(input("Enter second Number:"))
# c=int(input("Enter third Number:"))
# maximum(a,b,c)

# Area
def Area(length,breadth):
    Area=length*breadth
    return Area
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
result=Area(length,breadth)
print("Area:",result)

# sum of number from 1 to n
def sum(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
n=int(input("Enter the number"))
print("sum:",sum(n))