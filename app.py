import streamlit


def run_app(triggers, summary):
    streamlit.title('Triggers and summary for article')
    streamlit.write("Triggers for article: ")
    triggers.replace("-", "\n-")
    streamlit.write(triggers)
    streamlit.write("Summary of the article: " + summary)
