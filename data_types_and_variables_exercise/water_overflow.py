number = int(input())
capacity = 0

# Loop through each iteration from 0 to (number-1)
for i in range(0, number):
    # Take user input for the number of liters
    liters = int(input())

    # Check if adding the current liters to the current capacity exceeds 255
    if capacity + liters <= 255:
        # If true, update the capacity by adding the current liters
        capacity += liters
    else:
        # If adding the current liters exceeds 255, print an error message
        print("Insufficient capacity!")

# Print the final capacity
print(capacity)

#number = int(input())
#capacity = 0
#for i in range(0, number):
 #   liters = int(input())
  #  if capacity + liters <= 255:
   #     capacity += liters
    #else:
     #   print("Insufficient capacity!")
#print(capacity)


# number_of_lines = int(input())
# capacity = 255
# water_counter = 0
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if capacity - liters_of_water < 0:
#         print("Insufficient capacity!" )
#         continue
#     water_counter += liters_of_water
#     capacity -= liters_of_water
# print(water_counter)