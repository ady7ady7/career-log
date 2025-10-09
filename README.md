This will be a log of my current learning and coding activities, which will revolve around manual coding (with no AI assistance) in order to foster deep understanding and problem-solving skills.

The current main goal is to grasp data analyst's skillset, and the main areas of focus are SQL and Power BI, and later I might focus more on Python (it would be nice to practice it regularly, since I already have experience).
I might also work on simple ETL pipelines in Python that will feed my database with data.
As for the database, I might simply use local storage, and for testing connection purposes I might be using my PostgreSQL from DigitalOcean, mainly used as a storage for the market data I'm regularly collecting.

The goal here is not to create big data applications, but rather learn, test, and develop working solutions in a small scale.
I might be using AI after working on a given project to evaluate the code.

3.10.2025 
- I've created a Selenium instance, connected to a few sites and successfully got past the cookie button. Issues with scraping data from wakacje.pl - xpath imports seem to fail
 with Error: Message: no such element: Unable to locate element - even though I'm grabbing the seemingly correct elements by their XPATH. Doesn't work either solo or in a loop. The goal here
 is to be able to scrape them nicely and then put in a table. (2-3 hrs)
- I've also studied Microsoft's Power BI Course (1.5 hrs) and made some notes during that time. Feels like a perfect direction for me now.

6.10.2025
- I've completed the first day of my SQL for Data Analysis course, found and joined a Data Science community on Discord, where I did a basic research of current market situation, job requirements and learning possibilities (2 hrs)
- Studied Microsoft Power BI Course (2 hrs) - some notes and practice of different chart tpes - bar/column/pie/donut/treemap/line/stacked bar/columns - so far it seems to be very intuitive, and best learned through practice and multiple analysis/business cases
- Another scraping attempt with Selenium (scraping1-selenium.py) - I managed to skip the Cookie button again with locating and using .click() function, using Selenium's By method to identify the button by its XPATH. Failed to go further and actually scrape the top premieres from the ranking - even though the XPATH seems to be alright, Selenium is not able to find it - perhaps it's an issue connected with the iframes, but I didn't yet solve it. I might try again tomorrow (1hr)

7.10.2025
- Started the day with exercises from my SQL course - it took me some time and I had to check Postgresql docs (very useful btw), but I managed to correctly do a JOIN of two tables and extract data about distinct number of buyers who have purchased something at least once (1:M table relation) (1hr)
Postgresql docs - https://www.postgresql.org/docs/current/queries-table-expressions.html
- Followed up with an exercise from Datalemur - had serious issues here - even though it was labeled as easy, it required fairly complex subquery in my opinion (30 min). This task already required dividing into more subtasks - I've managed to get the first subtask done correctly, failed to do the second one though.
- Finished the first module of Microsoft's Power BI Course - going with high intensity here (2.5 hrs), the plan is to run through the course to ground my knowledge, and then upkeep and level up by doing regular report and dashboards based on free datasets
- Scraping in Selenium #2 - successfully managed to get past the Filmweb ad screen this time, and correctly located the rankingTypeSection container and the list of films  The only stage I have to get through now is correctly iterating through the films and extracting their names and scores (1 hr)

8.10.2025
- Started the day with another set of questions and an exercise from my SQL course - it wasn't too difficult for me today - checked Postgresql docs to deal with some issues, learned about the importance of parentheses in tagging/aggregating columns + it went quite well (45 minutes)
- Followed up with an exercise from Datalemur - chose LinkedIn easy task today, which was not that easy for me - I had to check Postgres docs and StackOverflow (No AI shortcuts in the learning process!). It was a single table SELECT and the goal was to select only those candidates that had ALL the required skill values. I used HAVING clause and chose only those candidates who had count(candidates.skill) of 3. (30 minutes)
- Finished another part of the Power BI course (still module 2, moving at a swift pace, but not too much, adjusting it to secure knowledge comprehension and practice) + downloaded a few custom themes, and followed up with an accessibility exercise + made some general notes in my Notion to describe good practices for building reports in Power BI (1.5 hrs)

9.10.2025
- Set of questions and an exercise from my SQL course - learned HAVING, although it was not necessary, the game changers were using OR and proper syntax with parentheses over all instances of defining all values of one argument in WHERE clause e.g. u.gender = 'Female' AND (age > 20 OR age > 60). The difficulty here was that the age was in two separate ranges that could not be defined with BETWEEN clause. The exercise was not too difficult, went pretty quick (30 minutes)
- Followed up with Datalemur -> today it was this one - https://datalemur.com/questions/sql-page-with-no-likes. I managed to solve it on my own using NOT IN clause to find all page_id's that weren't present in the second table page_likes. Had to use simple subquery for that task, and it wasn't that difficult (30 minutes)
- Finished another lesson in the Power BI course - this one's focused on hierarchies, sorting & filtering, and also very useful feature of Power BI - cross-highlighting and cross-filtering, a default cross-highlighting settings make all visuals highlight a particular fragment of data if clicked; this setting can also be changed to cross-filtering with a few clicks, which seems to be very useful (1 hr)
- Successfully finished the scraping attempt of Filmweb premieres! Managed to crush it with class name identification of page components - now it seems much easier! Planning to still practice and try to scrape other pages and content (1hr)
- Followed up with a very similar scraping code scraping3-selenium, to practice and scrape the leaderboard of new TV shows from Filmweb (20 mins)
- Created my first visual in Power BI on my own (cofeereport1.pbix.), using a dataset from Kaggle - I chose a very simple dataset on purpose, just to practise the basics and ground my knowledge about basic visualization types. I tried to make it accessible and present data in an understandable format.