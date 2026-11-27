
'''try:
    premium=int(input("Enter the premium amount:"))

    if  premium <=0:
        raise ValueError("Premium amount cannot be negative.")

except ValueError as ex:
    print("Error:", ex)

else:
    print("Premium amount is valid:", premium)

finally:
    print("Execution completed.")
    
    '''



# CUSTOM EXCEPTION
class InvalidAgeException(Exception):
    pass

try:
    age=int(input("Enter your age:"))

    if age<0:
        raise InvalidAgeException("Age cannot be Negative.")

except InvalidAgeException as ex:
    print("Error:", ex)

else:
    print ("Valid age:", age)



