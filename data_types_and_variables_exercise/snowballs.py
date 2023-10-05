count_balls = int(input())
best_ball = 0
best_time = 0
best_quality = 0
best_weight = 0

# Loop through each ball
for balls in range(count_balls):
    # Take input for weight, time, and quality of the ball
    weight = int(input())
    time = int(input())
    quality = int(input())

    # Calculate the value of the ball based on the provided formula
    value_of_ball = (weight / time) ** quality

    # Check if the current ball has a higher value than the best_ball
    if value_of_ball > best_ball:
        # If true, update the best_ball and related information
        best_ball = value_of_ball
        best_weight = weight
        best_quality = quality
        best_time = time

# Print the result
print(f"{best_weight} : {best_time} = {int(best_ball)} ({best_quality})")
