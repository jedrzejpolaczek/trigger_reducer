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

# APP URL
https://jedrzejpolaczek-trigger-reducer-run-pw2f8p.streamlitapp.com/

## OpenAI API key generator
https://beta.openai.com/account/api-keys

## Link to Fox13 news website
https://www.fox13now.com

# THOUGHTS
## Thought process behind creating the application
### More general
Due to my ADHD it's hard to describe Thought process. Is mamy od them first and ideas poping like  bubbles in soda but how bubbles in after the while their become more "steady".
Then I concentrate on one area and thought about problems of every people (I am one of them after all!) that can be solved. 
In these case I brainstorm many ideas and after that I starter to "thinkn in the way" od the problem for example I am getting up and browse news. In the bacground I am still hyped on news technologie so ideas how się this technology to what I am currently doing naturalny pop up.
### In details
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

## Thoughts about GPT-3
Nice and useful "toy". Do not get me wrong. I am splitting ideas into "toys" and "breakthroughs". Like steam engines where "breakthroughs" and all technology based on them are "toys". For sure will be soon outdated if Yann Lecun has wright (his new papers from June 27, 2022).
GPT-3 is one of the tools that bring joy to using technology and create this "need" to know how it works. For me it showed how much more I have to learn about AI. I only have generall idea how it work but I would need many days of full-time-job work to write something simillar.

## Main challenge
Time management (but for whom it isn't for work/fun after hours?), beside it finding a good (and free) web scraper.

## Conclusion
Still worth it, it was fun and gave some ideas for the future. Probably to finish this app as an addon.
