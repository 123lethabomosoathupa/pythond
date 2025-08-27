class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """
        Initialize the survey with a question.
        Prepare an empty list to store responses.
        
        Parameters:
        question (str): The survey question to ask participants.
        """
        self.question = question
        self.responses = []  # List to store all survey responses

    def show_question(self):
        """Display the survey question to the user."""
        print(self.question)

    def store_response(self, new_response):
        """
        Store a single response to the survey.
        
        Parameters:
        new_response (str): The participant's answer to the survey question.
        """
        self.responses.append(new_response)

    def show_results(self):
        """Display all the responses collected so far."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
