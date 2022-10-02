import os
import openai


def get_article_triggers_and_summary(article_text: str, open_ai_api_key: str) -> tuple:
    """
    Get triggers and summary of the article.

    article_text (str): article to be parsed to see if it contain any triggers and sum up it.
    open_api_key (str): openAI API key.

    return (str, str): potential triggers in article and summarization of it.
    """
    api_key_login(open_ai_api_key)

    triggers = get_triggers(article_text)
    summary = get_summary(article_text)

    return triggers, summary


def api_key_login(open_api_key: str=None, from_file: bool=False) -> None:
    """ 
    Guard function to not passing anyone who do not pass his own OpenAI API key. 
    
    open_api_key (str): openAI API key.
    from_file (bool): flag if we want to read openAI API key from file.
    """
    if from_file:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    else:
        openai.api_key = open_api_key


def get_triggers(article_text: str) -> str:
    """
    Get ptential triggers in article.
    
    article_text (str): article to be parsed to see if it contain any triggers.

    return (str): potential triggers in article.
    """
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_triggers_prompt(article_text),
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].text


def get_summary(article_text: str) -> str:
    """
    Create summarization for article text.

    article_text (str): article to be parsed to create summary of it.
    
    return (str): sum up of article.
    """
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_summary_prompt(article_text),
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text


def generate_triggers_prompt(article_text: str) -> str:
    """
    Generate prompt for listing triggers from articles.

    article_text (str): article to be parsed to see if it contain any triggers.
    
    return (str): prompt for getting triggers warnins from passed article.
    """
    return "List trigger warnings for text: {}".format(article_text)


def generate_summary_prompt(article_text: str) -> str:
    """
    Generate prompt for creating summary of the article.

    article_text (str): article to be parsed to create summary of it.
    
    return (str): prompt for getting triggers warnins from passed article.
    """
    return "In max 3 sentences sum up the text: {}".format(article_text)