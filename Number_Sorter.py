print("Hello! I can sort you list of numbers in ascending or descending order!")
nums = int(input("List of numbers separated by spaces: "))
print("How would you like me to sort your numbers?")
print("1. Ascending")
print("2. Descending")
how = int(input("1 or 2: "))
if how == '1':
   nums.sort()
   print(nums)
elif how == '2':
   nums.sort(reverse=True)
   print(nums)
else:
   print("Error")