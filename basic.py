print("hello")

#variable decalration
Customer_Name="payal"
Age=20
PolicyNumber=1220
print("Customer Name:",Customer_Name)
print("Age:",Age)
print("Policy Number:",PolicyNumber)

#data type
print(type(Customer_Name))
print(type(Age))
print(type(PolicyNumber))

#eligibility using if 
age=int(input("Enter the age:"))
if age >=18 :
  print("yor eligible")
print("under age")

# Premium Calculation
Sum_Assured=2000
rate=0.05
Premium=Sum_Assured * rate
print("Premium:",Premium)

# class and object
class policy:
  def __init__(self,policy_name,policy_number):
    self.policy_name=policy_name
    self.policy_number=policy_number

  def Display(self):
    print("policy name:",self.policy_name)
    print("Policy Number:",self.policy_number)

policy1=policy("lifeinsurence",112)
policy1.Display()