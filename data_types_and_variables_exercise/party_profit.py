companions = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    coins += 50 - companions * 2
    if day % 3 == 0:
        coins -= companions * 3
    if day % 5 == 0:
        coins += companions * 20
        if day % 3 == 0:
            coins -= companions * 2
print(f"{companions} companions received {(coins // companions)} coins each.")

companions = int(input())
days = int(input())
coins = 0

# Loop through each day
for day in range(1, days + 1):

    # If the day is a multiple of 10, reduce companions by 2
    if day % 10 == 0:
        companions -= 2

    # If the day is a multiple of 15, increase companions by 5
    if day % 15 == 0:
        companions += 5

    # Calculate coins based on certain conditions
    coins += 50 - companions * 2

    # If the day is a multiple of 3, subtract coins based on companions
    if day % 3 == 0:
        coins -= companions * 3

    # If the day is a multiple of 5
    if day % 5 == 0:
        # Add coins based on companions
        coins += companions * 20

        # If the day is also a multiple of 3, subtract additional coins based on companions
        if day % 3 == 0:
            coins -= companions * 2

# Print the result
print(f"{companions} companions received {(coins // companions)} coins each.")
