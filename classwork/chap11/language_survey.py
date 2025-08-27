from survey import AnonymousSurvey

# Define the survey question
question = "What language did you first learn to speak?"

# Create an AnonymousSurvey object with the given question
language_survey = AnonymousSurvey(question)

# Display the question to the user
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")

# Start a loop to collect responses
while True:
    # Ask the user for their answer
    response = input("Language: ")
    
    # If the user types 'q', break out of the loop (stop collecting answers)
    if response == 'q':
        break
    
    # Store the user's response in the survey
    language_survey.store_response(response)

# Thank participants for their input
print("\nThank you to everyone who participated in the survey!")

# Display the collected results
language_survey.show_results()
