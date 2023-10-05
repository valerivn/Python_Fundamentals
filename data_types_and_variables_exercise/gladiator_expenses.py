count_lost_fights: int = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
count_shield_broke = 0

# Iterate through each fight
for number in range(1, count_lost_fights + 1):
    # Check if the fight number is even
    if number % 2 == 0:
        # If true, add the helmet price to the total expenses
        total_expenses += helmet_price
    # Check if the fight number is divisible by 3
    if number % 3 == 0:
        # If true, add the sword price to the total expenses
        total_expenses += sword_price
    # Check if the fight number is both divisible by 2 and 3
    if number % 3 == 0 and number % 2 == 0:
        # If true, add the shield price to the total expenses
        total_expenses += shield_price
        # Increment the shield break counter
        count_shield_broke += 1
        # Check if the shield broke an even number of times
        if count_shield_broke % 2 == 0:
            # If true, add the armor price to the total expenses
            total_expenses += armor_price

# Print the total expenses with a formatted string
print(f"Gladiator expenses: {total_expenses:.2f} aureus")


number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmets_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // 6
total_armor_broken = total_shield_broken // 2
expenses = total_helmets_broken * helmet_price + \
    total_sword_broken * sword_price + \
    total_shield_broken * shield_price + \
    total_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")