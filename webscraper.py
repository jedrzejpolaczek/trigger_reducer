import newspaper


def get_article(article_url: str) -> str:
    """
    Get article from website from passed url and parsed it.

    article_url (str): link to the website with article.

    return (str): str containing parsed article text.
    """
    raw_article = get_raw_article(article_url)
    parsed_article = parse_article(raw_article)

    return parsed_article


def get_raw_article(article_url: str) -> str:
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
