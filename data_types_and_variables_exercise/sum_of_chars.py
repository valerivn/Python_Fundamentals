number_char = int(input())
sum_of_char = 0

# Loop through each character
for _ in range(number_char):
    # Take input for a character
    char = input()
    # Add the ASCII value of the character to the sum
    sum_of_char += ord(char)

# Print the result
print(f"The sum equals: {sum_of_char}")
