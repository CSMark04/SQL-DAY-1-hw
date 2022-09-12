# Given an integer return the integer with all the digits reversed:
# Must work for positive and negative numbers
# Input
from unicodedata import digit


x1=1234
x2=-1234

def rev(arr):
  
    arr = str(arr) 

    if arr[0] == '-':
        arr = arr.replace('-', '')
        return '-' + arr[::-1]
    else:
        return arr[::-1]

print(rev(x2))