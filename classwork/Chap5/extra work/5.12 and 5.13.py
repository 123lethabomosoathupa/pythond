# Welcome message for the quiz
print("Welcome to the quiz!") 

# Initialize the score to zero
score = 0

# Ask the first question and convert the answer to lowercase for consistency
answer = input("What is the capital of France? ").lower()

# Check if the answer is correct
if answer == "paris":
    print("Correct!")
    score += 1  # Increase score by 1
else:
    print("Oops, the correct answer is Paris.")

# Ask the second question (no lowercase conversion needed because it's numeric)
answer = input("What is 2 + 2? ")

# Check if the answer is correct
if answer == "4":
    print("Correct!")
    score += 1  # Increase score by 1
else:
    print("Oops, the correct answer is 4.")

# Print the final score out of 2 questions
print(f"Your final score is {score}/2.")

