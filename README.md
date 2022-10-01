# TASK
Signup on beta.openai.com to get GPT-3 access.

Utilizing https://streamlit.io/ or other preferred framework, build a simple GPT-3 based app to impress us with.

Publish it online and share url and your thoughts with us by answering the following questions:

What was your thought process behind creating the application?

What are your views on GPT-3, Codex and other modern AI technologies?

What was the biggest challenge in this task for you?

URL of your app:

Tips: Protect your app & api key either by request that users add their own API key like done in https://github.com/Shubhamsaboo/kairos_gpt3 or add password protection.

Preferred timeline for completion is about 48hrs. As stated if you cannot make the deadline let us know and we will move it appropriately.

Good luck and have fun!

# CONCEPT
1. Get the link to article.
2. Web Scraping news articles from link in Python 
* We will try: https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558 
* Ideal approach: we should try use hidden Markov models.
4. Run OpenAI GPT-3 Davinci model on text using prompt
* For list of triggers `List trigger warnings from text "{ARTICLE}"`
* For summary `Analyze text "{ARTICLE}" and answer on question "{HEADLINE}”`
* NOTE: Use GPT-3 Davinci model https://beta.openai.com/docs/models/content-filter
5. Display triggers and button to show summary of the article
6. After clicking "show summary" button show summary of article.

# TOOLSET
1. https://openai.com/api/
2. https://streamlit.io/
