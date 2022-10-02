import os

import openai
import newspaper


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


def get_article(article_url: str) -> str:
    """
    Get article from website from passed url.

    article_url (str): link to the website with article.

    return (str): str containing article text.
    """
    article = newspaper.Article(article_url)
    article.download()
    article.parse()

    return article.text


def parse_article(article_text: str) -> str:
    """ 
    Parse article text to reduce potential tokens.

    article_text (str): str containing article text.

    return (str): parsed str containing article text.
    """
    raw_article = repr(article_text)
    parsed_article = raw_article.replace("\\n", "")

    return parsed_article


def get_triggers(article_text: str) -> str:
    """
    Get ptential triggers in article.
    
    article_text (str): article to be parsed to see if it contain any triggers.

    return (str): ptential triggers in article.
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


def run(article_url):
    api_key_login("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")
    article_text = get_article(article_url)
    parsed_article_text = parse_article(article_text)

    triggers = get_triggers(parsed_article_text)
    summary = get_summary(parsed_article_text)

    print("\n\nTRIGGERS:" + triggers)
    print("\n\nSUMMARY:" + summary)