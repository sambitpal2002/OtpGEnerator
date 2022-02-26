#otp generator

import  random
otpgener=random.randint(000000,999999)
username=input("Username: ")
print("Hello ! ", username)
print("Otp for login is- ",otpgener)
password=input("Enter The otp for login")
if password==str(otpgener):
    print("Login Sucessful !!!")
else:
    print("Please enter valid input")
