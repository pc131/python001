import re
reg = re.compile("[a-z]+8?")
str = "ccc8"
print(reg.match(str))