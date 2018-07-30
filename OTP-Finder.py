# OTP finder program

# regular expressions

import re

string="dear customer your otp for transacton in icici bank is 989832. valid for 10 minutes only."                                                       # complete 
# compile regular ecxpressions

exp = re.compile('[0-9]{6}')
result= exp.search(string)
# matching regular expressions
print("")
print("OTP is : " , result[0])
