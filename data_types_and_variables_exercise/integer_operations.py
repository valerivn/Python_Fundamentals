first_num = int(input())
second_num = int(input())
third_num = int(input())
forth_num = int(input())
operation_number = (first_num + second_num) // third_num * forth_num
# operation_number = int((first_num + second_num) / third_num) * forth_num
print(operation_number)

# Prompt the user to enter the first integer and store it in the variable 'first_num'
first_num = int(input("Enter the first integer: "))

# Prompt the user to enter the second integer and store it in the variable 'second_num'
second_num = int(input("Enter the second integer: "))

# Prompt the user to enter the third integer and store it in the variable 'third_num'
third_num = int(input("Enter the third integer: "))

# Prompt the user to enter the fourth integer and store it in the variable 'forth_num'
forth_num = int(input("Enter the fourth integer: "))

# Perform the specified operations:
#   1. Add the 'first_num' and 'second_num'
#   2. Integer divide the sum by 'third_num'
#   3. Multiply the result by 'forth_num'
# The final result is stored in the variable 'operation_number'
operation_number = (first_num + second_num) // third_num * forth_num

# Print the final result along with a descriptive message
print("The final result is:", operation_number)
