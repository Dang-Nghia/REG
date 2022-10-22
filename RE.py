import re

str = 'enh yeu em lam'
patern = "^a"
match = re.match(patern, str)
# If-statement after search() tests if it succeeded
if match:
  print("tim kiem thanh cong")
else:
  print('tim kiem khong thanh cong')
