import openai
from ReadImage import read_text

"""
This is a draft as well (mostly from GPT itself); I haven't made the payment, 
so we can't use it yet. Just an idea of how to use LM to get anwers. 
(openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.)

This file evaluates a food based on ingredient list, while the other things 
we've been doing deals with nutrition label. 

Theoretically, if the rating in nutrition or ingredient is below a certain 
threshold, we label it as bad. If we have time, we can do allergens too 
using keywords from LM.
"""

def author():
    """
    Returns:
       author name in list
    """
    return ['Rachel Yu-Wei Lai']

def language_model(file_name):
    """
    This function takes in a file name of ingredient list, reads the text, then enters the
    info for the language model to evaluate, which will end up producing a score.
    ------------------
    Parameters: 
    file_name: file name of ingredient list in str
    ------------------
    Returns: chatGPT's response in str
    """
    
    # Set your API key
    api_key = "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"

    # Define your prompt (the text you want to provide as input)
    ingredients = read_text(file_name)
    prompt = f"Give this food a rating out of 10 in terms of healthy level, based on the below ingredient list alone: {ingredients}."

    # Make an API request
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can specify different engines depending on your needs.
        prompt=prompt,
        max_tokens=10,  # Adjust the response length as needed.
        api_key=api_key
    )

    # Get the generated response
    answer = response.choices[0].text

    print("Answer:", answer)
    
    return answer

###########################################################
if __name__ == "__main__":
    file_name = ''
    language_model(file_name)