first_index = int(input())
second_index = int(input())

# Loop through each character code in the specified range
for char in range(first_index, second_index + 1):
    # Convert the character code to its corresponding symbol
    symbol = chr(char)
    # Print the symbol with a space as the end parameter to print on the same line
    print(symbol, end=" ")



# first_index = int(input())
# second_index = int(input())
# symbol = ""
# for char in range(first_index, second_index + 1):
#     symbol += chr(char) + " "
# print(symbol)