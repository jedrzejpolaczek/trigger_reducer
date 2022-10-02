import streamlit

# Local imports
from webscraper import get_article
from ai import get_article_triggers_and_summary


def run_app():
    streamlit.title('Show triggers and summary for FOX13 article!')
    open_ai_api_key = streamlit.text_input(
        "OpenAI API key", 
        ""
    )
    article_url = streamlit.text_input(
        "URL to article", 
        "https://www.fox13now.com/news/local-news/2-people-killed-in-crash-on-i-215"
    )

    article_text = get_article(article_url)
    triggers, summary = get_article_triggers_and_summary(article_text, open_ai_api_key)

    streamlit.write("TRIGGERS:")
    for trigger in triggers.split("-"):
        streamlit.write(trigger)
    streamlit.write("SUMMARY:")
    streamlit.write(summary)


run_app()
