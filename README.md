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
## For MVP
1. User need to pass their own OpenAI API key.
2. User will pass link to the article.
3. App will scrap article from URL. 
4. OpenAI GPT-3 Davinci model will run on text using prompts:
* For list of triggers `List trigger warnings from text "{ARTICLE}"`
* For summary `Analyze text "{ARTICLE}" and answer on question "{HEADLINE}”`
5. App will display triggers and button to show summary of the article.

## For ideal approach
1. Whole app should be addon to webbrowser.
2. App/addon should work in that way, that you move the cursor (or press screen longer) over the link, and pop up window will... pop up with triggers and short summary.
3. Web Scraping: currently we are using Newspaper3k lib. That approach will not work with any articles URL. To solve it we should use hidden Markov models (but it is a topic for PhD...).

# TOOLSET
1. https://openai.com/api/
2. https://streamlit.io/

# THOUGHTS
## What was your thought process behind creating the application?
0. (in bacground): brainstorming all the time and writing down all ideas.
1. Read what about OpenAI.
2. See examples of usage of OpenAI on OpenAI website.
3. Play with OpenAI.
4. Looks for other OpenAI examples and simillar solutions/products.
5. Choose few topics based on that if I can implement MVP for it in short time and if it have potential to develop in the future.
6. Choose one idea and see similar solutions.
7. Create my own draft of code structure (in bullet points) / solution.
8. Look at simillar code structure.
9. Write URL scraper "module" code with docs.
10. Test URL scraper "module" code.
11. Write OpenAI "module" code with docs.
12. Test OpenAI "module" code.
13. Test if "modules" works together.
14. Write app "module" code with docs.
15. Test app "module" code.
16. Test if "modules" works together.

## What are your views on GPT-3, Codex and other modern AI technologies?
Nice and useful "toy". Do not get me wrong. I am splitting ideas into "toys" and "breakthroughs". Like steam engines where "breakthroughs" and all technology based on them are "toys". For sure will be soon outdated if Yann Lecun has wright (his new papers from June 27, 2022).
GPT-3 is one of the tools that bring joy to using technology and create this "need" to know how it works. For me it showed how much more I have to learn about AI. I only have generall idea how it work but I would need many days of full-time-job work to write something simillar.
## What was the biggest challenge in this task for you?
Time management (but for whom it isn't for work/fun after hours?), beside it finding a good (and free) web scraper.

## Conclusion
Still worth it, it was fun and gave some ideas for the future. Probably to finish this app as an addon.