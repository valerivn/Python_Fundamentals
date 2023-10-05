key_number = int(input())
count_lines = int(input())
massage = ""

# Loop through each character
for char in range(count_lines):
    # Take user input for a character and convert it to its ASCII value
    character = ord(input())
    # Add the character shifted by the key_number to the massage
    massage += chr(character + key_number)

# Print the result
print(massage)
