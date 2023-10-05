first_number = int(input())
second_number = int(input())

# Print the initial values of the variables
print(f"Before:\na = {first_number}\nb = {second_number}")

# Swap the values of the two variables using a temporary variable
temporary_number = first_number
first_number = second_number
second_number = temporary_number

# Print the values of the variables after swapping
print(f"After:\na = {first_number}\nb = {second_number}")
