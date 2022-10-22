import re

str = "dau ai biet lan gap luc do ngoi ke ben nhau la lan cuoi cung"

partern = "[^trang]"

match = re.search(partern, str)

if match:
  print("da tim kiem thanh cong")
else:
  print("tim kiem da that bai")
