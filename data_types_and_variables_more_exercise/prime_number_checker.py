number = int(input())
counter = 0

# Check if the number is greater than 1
if number > 1:
    # Loop through numbers from 2 to (number-1)
    for i in range(2, number):
        # Check if the number is divisible by i
        if number % i == 0:
            # If true, increment the counter
            counter += 1

# Check if the counter is greater than 0
if counter > 0:
    # If true, print "False"
    print("False")
else:
    # If not true, print "True"
    print("True")
