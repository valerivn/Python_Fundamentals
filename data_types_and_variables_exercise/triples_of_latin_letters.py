number = int(input())

# Outer loop: Iterating from 0 to (number-1)
for i in range(number):
    # Middle loop: Iterating from 0 to (number-1)
    for j in range(number):
        # Innermost loop: Iterating from 0 to (number-1)
        for k in range(number):
            # Printing a combination of characters based on loop variables i, j, and k
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
