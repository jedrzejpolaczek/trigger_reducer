# Local imports
from webscraper import get_article
from ai import get_article_triggers_and_summary
from app import run_app


def run(article_url, open_ai_api_key):
    article_text = get_article(article_url)

    triggers, summary = get_article_triggers_and_summary(article_text, open_ai_api_key)

    run_app(triggers, summary)


run(
    'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/',
    "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"
)



