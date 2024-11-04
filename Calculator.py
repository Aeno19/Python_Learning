num1 = float(input("number 1: "))
num2 = float(input("number 2: "))
action = str(input("operation: ")
if ':' in action or '/' in action:
   if num2 != 0
      result = num1 / num2
      print("Answer:", result)
   else:
      print("Error - division by 0")
elif '+' in action:
   result = num1 + num2
   print("Answer:", result)
elif '-' in action:
   result = num1 - num2
   print("Answer:", result)
elif '*' in action or '•' in action:
   result = num1 * num2
   print("Answer:", result)
else:
   print("Error - use +, -, * (•) or /(:) operators")