# install the necessary libraries
import os
import openai
from colorama import Fore, Style

# using the api_key of openai
openai.api_key = "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"

# setting parameters
ANSWER_SEQUENCE = "\nAI:"
QUESTION_SEQUENCE = "\nHuman: "
TEMPERATURE = 0.5
MAX_TOKENS = 500
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6

# number of questions we want to add into context
MAX_CONTEXT_QUESTIONS = 10


# function including all the set parameters for the openai model that is being used
def chatgpt_response(prompt):
    """
    This function takes the prompt given by user as input and returns the response from the model.

    Parameters: 
    prompt (str datatype): Input to the function
    Returns the response from the model
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    )
    return response.choices[0].text


def main():

    # clear the terminal
    os.system("cls")

    print(Fore.MAGENTA + Style.BRIGHT + "Ask your questions here..." + Style.RESET_ALL)
    print()

    # store previous questions and answers to keep track
    previous_questions_answers = []

    while True:

        # question from user
        n_question = input(Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL)

        # to close the chatbot
        if n_question == "close":
            print(
                Fore.CYAN
                + Style.BRIGHT
                + "ChatGPT: "
                + Fore.MAGENTA
                + "Sure! Have a great day :)"
                + Style.RESET_ALL
            )
            break

        # Building context for next questions
        context = ""
        for question, answer in previous_questions_answers[-MAX_CONTEXT_QUESTIONS:]:
            context += QUESTION_SEQUENCE + question + ANSWER_SEQUENCE + answer

        # adding the new question to the end of the context
        context += QUESTION_SEQUENCE + n_question + ANSWER_SEQUENCE

        # getting response from the function for the input context
        response = chatgpt_response(context)

        # adding new question and answer to the previous_questions_answers list
        previous_questions_answers.append((n_question, response))

        # printing the response
        print(Fore.CYAN + Style.BRIGHT + "ChatGPT: " + Style.NORMAL + response)
        print()


if __name__ == "__main__":
    main()
