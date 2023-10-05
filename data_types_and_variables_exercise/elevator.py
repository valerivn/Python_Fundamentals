# Read the number of people (N) from the user
people = int(input())

# Read the capacity of the elevator (P) from the user
capacity = int(input())

# Initialize a variable to count the number of courses needed
count_course = 0

# Start a loop that continues until there are no more people to transport
while people != 0:
    # Check if there are more people than the capacity of the elevator
    if people > capacity:
        # If yes, subtract the capacity from the total people
        people -= capacity
        # Increment the count of courses by 1
        count_course += 1
    else:
        # If no, it means all remaining people can be transported in one course
        # So, set the number of people to 0 to exit the loop
        people -= people
        # Increment the count of courses by 1
        count_course += 1

# Print the total number of courses needed
print(count_course)


# people = int(input())
# capacity = int(input())
# count_course = 0
# while people != 0:
#     if people > capacity:
#         people -= capacity
#         count_course += 1
#     else:
#         people -= people
#         count_course += 1
# print(count_course)

#from math import ceil
#people = int(input())
#capacity = int(input())
#count_course = ceil(people / capacity)
#print(count_course)

#people = int(input())
#capacity = int(input())
#count_course = people // capacity
#if people % capacity != 0:
#    count_course += 1
#print(count_course)