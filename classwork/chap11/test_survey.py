# test_survey.py
import pytest
from survey import AnonymousSurvey

# -------------------------------
# Fixture to provide a reusable survey instance
# -------------------------------
@pytest.fixture
def language_survey():
    """
    Create and return a survey instance that will be available to all test functions.
    """
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)
    return survey

# -------------------------------
# Test storing a single response
# -------------------------------
def test_store_single_response(language_survey):
    """
    Test that a single response is stored properly in the survey.
    """
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

# -------------------------------
# Test storing multiple responses
# -------------------------------
def test_store_three_responses(language_survey):
    """
    Test that three individual responses are stored properly in the survey.
    """
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    # Ensure all responses are in the survey
    for response in responses:
        assert response in language_survey.responses


# python -m pytest test_survey.py
