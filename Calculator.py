while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit")

    choice=int(input("Enter your choice"))
    if choice == 5:
       print("calculator closed")
       break

    A=int(input("Enter First Number"))
    B=int(input("Enter second Number"))

    if choice == 1:
       print("Addition:",A+B)
    elif choice ==2:
       print("Substraction:",A-B)
    elif choice == 3:
       print("Multiplication:",A+B)
    elif choice ==4:
       print("Division:",A-B)
    else :
       print("Invalid Choice")


      #  using function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
   print("1.Addition")
   print("2.Substraction")
   print("3.multiplication")
   print("4.Division")
   print("5.Exit")

   choice=int(input("Enter your choice"))


   if choice==5:
    print ("Calculator closed")
    break

   a=int(input("Enter the first number:"))
   b=int(input("Enter the second number:"))
   
   if choice ==1 :
      print("addition:",add(a,b))
   elif choice ==2 :
      print("substraction:",sub(a,b))
   elif choice ==3 :
      print("Multiplication:",mul(a,b))
   elif choice ==4 :
      print("Divisin:",div(a,b))  
   else :
      print("invlid choice")