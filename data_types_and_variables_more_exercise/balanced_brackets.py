number_lines = int(input())
count_open = 0
count_close = 0
is_valid = True

# Loop through each iteration from 0 to (number_lines-1)
for i in range(number_lines):
    # Take user input for a line
    input_line = input()

    # Check if the input line is an opening parenthesis
    if input_line == "(":
        count_open += 1
    # Check if the input line is a closing parenthesis
    elif input_line == ")":
        count_close += 1

    # Check if the difference between the count of closing and opening parentheses is greater than 1
    if abs(count_close - count_open) > 1:
        # If true, set is_valid to False and break out of the loop
        is_valid = False
        break

# Check if the counts of closing and opening parentheses are equal and is_valid is True
if count_close == count_open and is_valid:
    # If true, print "BALANCED"
    print("BALANCED")
else:
    # If not true, print "UNBALANCED"
    print("UNBALANCED")
