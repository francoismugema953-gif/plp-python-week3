# Start with the given list of scores
scores = [72, 45, 90, 61, 38]

# Initialize counters and sum variable
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
      grade = "F"

    # Print each score with its grade on its own line
    print(f"Score: {score}, Grade: {grade}")

    # Track passes and fails (passing is 50 or more)
    if score >= 50:
      passed_count += 1
    else:
      failed_count += 1

    # Add to the total sum of scores
    total_score += score

# Calculate average
average = total_score / len(scores)
rounded_average = round(average, 1)

# Print final results
print(f"\nNumber that passed: {passed_count}")
print(f"Number that failed: {failed_count}")
print(f"Average score: {rounded_average}")
