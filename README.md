This will be a log of my current learning and coding activities, which will revolve around manual coding (with no AI assistance) in order to foster deep understanding and problem-solving skills.

The current main goal is to grasp data analyst's skillset, and the main areas of focus are SQL and Power BI, and later I might focus more on Python (it would be nice to practice it regularly, since I already have experience).
I might also work on simple ETL pipelines in Python that will feed my database with data.
As for the database, I might simply use local storage, and for testing connection purposes I might be using my PostgreSQL from DigitalOcean, mainly used as a storage for the market data I'm regularly collecting.

The goal here is not to create big data applications, but rather learn, test, and develop working solutions in a small scale.
I might be using AI after working on a given project to evaluate the code.

3.10.2025 (Day 1)
- I've created a Selenium instance, connected to a few sites and successfully got past the cookie button. Issues with scraping data from wakacje.pl - xpath imports seem to fail
 with Error: Message: no such element: Unable to locate element - even though I'm grabbing the seemingly correct elements by their XPATH. Doesn't work either solo or in a loop. The goal here
 is to be able to scrape them nicely and then put in a table. (2-3 hrs)
- I've also studied Microsoft's Power BI Course (1.5 hrs) and made some notes during that time. Feels like a perfect direction for me now.

6.10.2025 (Day 2)
- I've completed the first day of my SQL for Data Analysis course, found and joined a Data Science community on Discord, where I did a basic research of current market situation, job requirements and learning possibilities (2 hrs)
- Studied Microsoft Power BI Course (2 hrs) - some notes and practice of different chart tpes - bar/column/pie/donut/treemap/line/stacked bar/columns - so far it seems to be very intuitive, and best learned through practice and multiple analysis/business cases
- Another scraping attempt with Selenium (scraping1-selenium.py) - I managed to skip the Cookie button again with locating and using .click() function, using Selenium's By method to identify the button by its XPATH. Failed to go further and actually scrape the top premieres from the ranking - even though the XPATH seems to be alright, Selenium is not able to find it - perhaps it's an issue connected with the iframes, but I didn't yet solve it. I might try again tomorrow (1hr)

7.10.2025 (Day 3)
- Started the day with exercises from my SQL course - it took me some time and I had to check Postgresql docs (very useful btw), but I managed to correctly do a JOIN of two tables and extract data about distinct number of buyers who have purchased something at least once (1:M table relation) (1hr)
Postgresql docs - https://www.postgresql.org/docs/current/queries-table-expressions.html
- Followed up with an exercise from Datalemur - had serious issues here - even though it was labeled as easy, it required fairly complex subquery in my opinion (30 min). This task already required dividing into more subtasks - I've managed to get the first subtask done correctly, failed to do the second one though.
- Finished the first module of Microsoft's Power BI Course - going with high intensity here (2.5 hrs), the plan is to run through the course to ground my knowledge, and then upkeep and level up by doing regular report and dashboards based on free datasets
- Scraping in Selenium #2 - successfully managed to get past the Filmweb ad screen this time, and correctly located the rankingTypeSection container and the list of films  The only stage I have to get through now is correctly iterating through the films and extracting their names and scores (1 hr)

8.10.2025 (Day 4)
- Started the day with another set of questions and an exercise from my SQL course - it wasn't too difficult for me today - checked Postgresql docs to deal with some issues, learned about the importance of parentheses in tagging/aggregating columns + it went quite well (45 minutes)
- Followed up with an exercise from Datalemur - chose LinkedIn easy task today, which was not that easy for me - I had to check Postgres docs and StackOverflow (No AI shortcuts in the learning process!). It was a single table SELECT and the goal was to select only those candidates that had ALL the required skill values. I used HAVING clause and chose only those candidates who had count(candidates.skill) of 3. (30 minutes)
- Finished another part of the Power BI course (still module 2, moving at a swift pace, but not too much, adjusting it to secure knowledge comprehension and practice) + downloaded a few custom themes, and followed up with an accessibility exercise + made some general notes in my Notion to describe good practices for building reports in Power BI (1.5 hrs)

9.10.2025 (Day 5)
- Set of questions and an exercise from my SQL course - learned HAVING, although it was not necessary, the game changers were using OR and proper syntax with parentheses over all instances of defining all values of one argument in WHERE clause e.g. u.gender = 'Female' AND (age > 20 OR age > 60). The difficulty here was that the age was in two separate ranges that could not be defined with BETWEEN clause. The exercise was not too difficult, went pretty quick (30 minutes)
- Followed up with Datalemur -> today it was this one - https://datalemur.com/questions/sql-page-with-no-likes. I managed to solve it on my own using NOT IN clause to find all page_id's that weren't present in the second table page_likes. Had to use simple subquery for that task, and it wasn't that difficult (30 minutes)
- Finished another lesson in the Power BI course - this one's focused on hierarchies, sorting & filtering, and also very useful feature of Power BI - cross-highlighting and cross-filtering, a default cross-highlighting settings make all visuals highlight a particular fragment of data if clicked; this setting can also be changed to cross-filtering with a few clicks, which seems to be very useful (1 hr)
- Successfully finished the scraping attempt of Filmweb premieres! Managed to crush it with class name identification of page components - now it seems much easier! Planning to still practice and try to scrape other pages and content (1hr)
- Followed up with a very similar scraping code scraping3-selenium, to practice and scrape the leaderboard of new TV shows from Filmweb (20 mins)
- Created my first visual in Power BI on my own (cofeereport1.pbix.), using a dataset from Kaggle - I chose a very simple dataset on purpose, just to practise the basics and ground my knowledge about basic visualization types. I tried to make it accessible and present data in an understandable format. (2hr)
- As life just presented a real use-case for a scraper, I spent another 1+ hr to figure out how to scrap data from Otodom - it's not finished yet in a form I want it, but I might finish soon - the issue now is to operate with multiple windows, and maybe also create limits to not get blocked (1hr)

10.10.2025 (Day 6)
- Set of questions and an exercise from my SQL course - today's focus was on extracting date parts from timestamps - I used EXTRACT(MONTH from x) = 5, but you can also use date_part('month', x) = 5; It wasn't that difficult once I found that, but also they wanted me to find the 2nd person, not the first, and out of rush I chose wrong answer, intuitively thinking it's all about the first person who created an account. (30 mins)
- Followed up with Datalemur exercise - Tesla Unfinished Parts Easy task - that was really easy - it took me literally a minute to solve - the easiest so far, perhaps because it was directly related to extracting data (2 mins)
- Today's a busy day and it might be difficult to do much more, writing this just in case.
- Brushed up the Otodom scraper - it currently runs two separate loops - the first one scrolls to the bottom of the page, extracting all the links to all apartments; then the second loop takes over to iterate over all links, opening the window, locating the description using the procedure developed yesterday, and saving it in a list - later can be turned into a pandas Series to quickly delete duplicates. There are some issues like sometimes the webdriver still gets stuck as some advertisements have very long first section, and the scroll length is not enough to get to the button - this causes the "Wiadomość" button to intercept our click, basically blocking the code. 
To prevent that, I should develop scrolling until the button is clearly visible and can't be intercepted - this is perfectly doable.
After this issue is dealt with, I have to implement pagination, actually merging our descriptions with links, and filtering descriptions for the words we need (2 hr)

13.10.2025 (Day 7, after a weekend)
- Studied Lesson 2 from the SQL course - it contained some great tips about code writing and descriptions of basic filtering clauses like WHERE, ORDER BY, LIMIT, GROUP BY, DISTINCT, AND/OR, IS NULL/ IS NOT NULL, BETWEEN. The lesson was great, I took extensive notes on every important aspect. (1 hr)
- Finished today's weekly test (didn't go too bad, but I've made some partial errors in multi-choice questions - I chose the most important answers, but omitted less obvious choices - got 7/9 points) (15 mins)
- Finished today's SQL exercises (10 mins) - went by really fast and EASY, compared to the last week, and I must admit that my teacher's tips about code writing ARE A GAME CHANGER. I had to use Postgres docs to check joining rules, as I still don't remember it that well, but it was fast.
- Followed up with Datalemur exercise - NY Times Laptop vs Mobile Viewership - I crushed it - had to use two easy subqueries and aliases, it went by smoothly, without any issues - thanks to my teacher's coding tips that was a piece of cake (3 mins)
- Followed up with another Datalemur exercise later - Facebook Average Post Hiatus (Part 1) - it was supposed to be easy, but I struggled so hard with it and I definitely have to work on extracting dates and working on them, as it was a nightmare - I had to use solution in the end, as I don't want to wait in this complete lack of progress state. I'll try to get back to that and review it frequently to get good at date extraction and operations on dates (1.5 hrs)
- Followed up with another lesson from Microsoft PBI course - today's learning was rather short, as I had a busy day (20 mins)

14.10 (Day 8)
- Started with exercises from the SQL course - today I've encountered extracting dates again and that was difficult - I couldn't solve the problem; Followed up with exercises designed on the basis of my database by Perplexity - I've got 8/10 exercises and learned how to use EXTRACT with dates quite consistently - there's still more to learn, but I feel more confident with dates. (2 hrs)
- Followed up with Datalemur exercise - had to use EXTRACT dates there so it fitted perfectly, and thanks to the exercises I've done today - it was a breeze, compared to yesterday's struggle (5 minutes)
- Finished another module of PBI Course on Coursera (1.5 hrs)

15.10 (Day 9)
- Finished morning SQL course exercises (30 mins) - today I practiced using HAVING and combining multiple requirements in WHERE clause
- Followed up with Datalemur exercise - 30 mins - it was doable, but needed some time and using HAVING was also very helpful here to maintain my subquery properly
- Done another part of PBI Course on Coursera - it's currently going through a bit boring stage of theory, but there will be more practice soon, and I will also have to actually purchase PBI Service as the Desktop version will not be suitable for dashboards and it has certain limitations (30 mins)

16.10.25 (Day 10)
- Started the day with my SQL course exercises - today it was easy and quick, without the extra question for some reason (20 mins) 
- Followed up with Datalemur exercise (20 mins) - it was rather easy today, I had brief issue when trying to use COUNT in GROUP BY, but it was not necessary (and also impossible)
- Worked on my Otodom scraper - made some serious progress today - I've used Claude to compute some ideas quicker, but all the reasoning was mine and definitely felt like a great learning experience: created a reliable scroll to button method for consistent scraping, merged links and descriptions into a Pandas df, built a filtering method for descriptions (looking for garaż and similar terms), build a filtering method for the upper section of ads and fixes numerous issues/bugs that occured during the development). I'm very close to the finish line with this project - planning to implement pagination, and perhaps title filtering as well - the rest is done! In the end, we could perhaps also put the code into a proper file structure in a separate folder, but currently it's not more than 150 lines of code - IMO it's still manageable and should be readable - trying to maintain proper labeling with comments (3 hr)

17.10.25 (Day 11)
- Morning SQL questions/exercises routine - the course now consists of ONLY code-based questions, and that's great and feels a lot better than the theoretical questions that were there at the beginning. Enjoying these tasks a lot, and I've managed to quickly get through today's exercises - practiced using wildcards today (_ for single chars and % for any number of chars), and some combined WHERE filters - I'm feeling pretty confident with these on the current level of difficulty. (30 mins)
- Followed up with a Datalemur exercise, as always. Today it was an Amazon task for calculating average star ratings for different products - it was easy for me and I've quickly wrote the query - there was a little twist though, as the results were to be given rounded to 2 decimals, but it could be very easily achieved with the ROUND function: ROUND(AVG(stars), 2). An interesting observation that I made today was that GROUP BY actually accepts the EXTRACT function/clause, and I remember it doesn't accept functions like COUNT. (10 mins)
- ADDED PAGINATION AND FINISHED the Otodom scraper (scraping5-selenium-otodom.py)! The pagination component is very simple, as we start from a counter of 1 and a set int of max_pages, and enclose the whole scraping procedure in a while loop, which works until our current page is lower than the max_pages. I chose to follow this implementation, since the code for my scraper is strictly sequential. At the end of the sequence we simply jump to the next page, increase the counter, and since the while condition is still in place, we automatically follow the process once again for the next page, until we hit the counter :)). (3 hr, including error handling below)

I've also enclosed the whole scraping code in a try-except block with finally block to handle VERY RARE(1 in 200~ pages, based on my observations) case where we encounter 404 error during scraping. It causes me to lose all the scraped ads, and this 
will make us save the results. Not sure what's the cause of the 404 error - as if the ad we're trying to go to gets deleted before we manage to click it, but it's unlikely. Perhaps it's caused by some limits. Anyway, for now I decided I'm not resolving the error itself, but handling it, as it's very rare, inconsistent, it would probably take a lot of time to actually diagnose the cause of it, and I don't think it's worth wasting time on it in this particular case.

Perhaps the next step would be to put everything in a nice method structure or maybe even different files, but it's 160 lines of code including vertical spaces and comments, and I think the code looks rather clear. One thing that might be a bit scary for new people are the indentations - they were introduced step by step, when creating next methods. I'm unsure if any dev might have trouble reading this, but I'd love to find out! Anyway, I'll think about it.

- I discovered a serious issue - it seems that I'm iterating through page 2 repeatedly, instead of actually moving forward
I've changed the location of driver.current_window_handle, as it was put before the loop, causing us to stay in page1 -> page2 loop, but it didn't solve the issue.

We need a more robust solution:
- check the handles of the buttons (if they change and if so, how)
- check manually the flow of being on page 2 and going to page 3
- implement actual page-checking using the handles instead of hardcoding page_number and incrementing it automatically each time

18.10.25 (Day 12, weekend - Saturday)
- Even though it's the weekend, I've downloaded a dataset from Kaggle with job listings and cleaned data a bit. I've explored functions in Power Query - used Perplexity's instructions for that, as it's my first time in PQ, and while it's not that intuitive without experience, I must say that it isn't difficult and very logical once you see how it works. I've got some experience with data and with instructions in went down pretty quickly and easily. I'll have to experiment more with that, already seeing how useful this is. Anyway, the dataset is prepared and will probably work as a base for my next PBI report(1 hr)

20.10.25  (Day 13)
- Started the day with Lesson 3 from my SQL Course - it was a very useful journey through aggregate functions, the level of selection and GROUP BY function. We also discussed the difference between the order of SQL clauses and the order of actual SQL operations (it explains a lot of things going on there e.g. why aliases won't work with HAVING clause, but they will work with ORDER BY etc.). Great lesson and I took notes (1 hr)
- Followed up with SQL test from week2, nailed it!
- Done today's SQL exercises (went pretty well and it was a great practice of the concepts I've learned today) and followed up with a Datalemur SQL Exercise - as for Datalemur, it was a bit tricky and I had to check the hint, as I wasn't sure how to approach it - it was a good idea, as the task required me to use INNER JOIN, which was my first time actually seeing that. Once I've done that, it was pretty easy, just had to filter data with WHERE and set aliases to get the required output (1 hr)

21.10.25 (Day 14)
- Started the day with SQL course exercises + Datalemur exercise (1 hour)
- Followed up with an evening session with the PBI course (1.5 hr)

22.10.25 (Day 15)
- Started with daily portion of SQL exercises from my course - today I practiced GROUP BY on different aggregation levels struggled a bit with the last question (advanced, additional one), where we had to filter users who WERE NOT in another table.
It was problematic, I tried to use standard JOIN first with a subquery and then use pseudo code trying things like users.id NOT IN (subquery) - but it all resulted in syntax errors.

I had to look it up and found a solution WITH practically the same logic, but with correct syntax, so called ANTI JOIN.

SELECT COUNT(DISTINCT(u.id)) AS number_of_users
FROM users u 
WHERE NOT EXISTS
	(SELECT t.id FROM transactions t 
	WHERE u.id = t.user_id)
    
So here we also have a SUBQUERY, but this time with WHERE NOT EXISTS, and the subquery also uses WHERE, and not join.
Anyway, it worked and it was great (1 hr)

- Followed up with another exercise from Datalemur - it was supposedly easy, but not for me - it was about calculating the CTR for an app in a specified year. I figured out a solution with subquery to find clicks and then divided them by the total amount of actions. The issue was that subquery returns only 1 column, which means it returned the total amount of clicks, and then they were attributed to BOTH apps, instead of being attributed to their respective app. Because of that, although the rest of the logic was working and I was calculating the % rate for the apps, the results were wrong!

I had to figure out a different solution and it took some time, but I finally looked up a solution and used the SQL equivalent of Python if clause - CASE WHERE -> THEN -> ELSE -> END, I've rewritten clicks and impressions separately with CASES, and counted them with a simple formula:
CASE WHERE event_type = 'click' THEN 1 ELSE 0 END as clicks etc.; then I added SUM to calculate them and check it it works correctly - when I was sure it does, I finally repeated the solution from my first try - deleted aliases (as clicks/as impressions), multiplied the clicks by 100.0 (as float was requested in the task), and then divided them by the sum of impressions, and obviously ROUNDED everything to get the required 2 decimals, and used GROUP BY by app_id, to get the final solution. It was very satisfying to finally finish (1 hr)


23.10.25 (Day 16)
- Started the day with a pretty nice session with SQL exercises - today's session was doubled as we had an extra set of exercises due for the end of the week. I've practiced GROUP BY and aggregation levels, but also used the opportunity to practice CASE WHEN, as there were at least two perfect uses. I've managed to get 7/8 and 13/13 in the two sets, completing over 20 exercises and it feels good to start the day this way. Feeling good with my current SQL skill. (2 hr)
- Followed up with another module of PBI Course (1 hr)
- Started ML course - today is my first try with it and now it mainly focuses on Python basics - it's nice and it looks like I'm managing to deal with these things without any problems - it will help me strenghten my beliefs in my Python skills(1 hr)
- Went through a looong session of PBI course to finish it and it - it was a useful course and I practiced all of the basic functions, and even learned some DAX functions - they seem to be very simple, at least the basic ones. As for Power BI in general, I definitely need practice if I want to get and maintain a high skill level - although in general this isn't anything super interesting, and I'm not entirely sure I will be using it frequently in my journey. I'm pretty sure if I have to use it, I will be able to adapt and remind myself how it works pretty quickly, especially under supervision. (2.5 hrs)

24.10.25 (Day 17)
- I started the day with exercises from my SQL Espresso course - went very well today - we're continuing the exercises on GROUP BY and aggregate functions in all sorts of questions. Feeling stronger with each day.
BUT!!! I realized that I crush even the advanced tasks and then realize I've lost a point or two because I did not read the instructions in the simple tasks carefully - e.g. I calculated the retired people's numbers properly, BUT TOTALLY MISSED THAT I ONLY HAVE TO COUNT THE RETIRED PEOPLE FROM POLAND. Another mistake was calculating the highest total sales amount instead of the lowest. These aren't logical errors or issues with understanding SQL, but rather being a bit too fast sometimes.
I HAVE TO REMIND MYSELF TO READ EACH QUESTION AT LEAST 3 TIMES AND I WILL DEFINITELY IMPROVE IN THIS ASPECT (1 hr)
- Followed up with an exercise from Datalemur (TikTok Second Day Confirmation - Easy), where I had to find users who confirmed their sign up exactly 1 day after its date. It wasn't too difficult at this point, took me 5~ minutes to solve it - started with a simple join and grabbing the relevant columns and checking whether I got what I need.
To find the days, I simply extracted Days in both dates (signup_date and confirmation_date) and substracted the first from the second one. I used HAVING for that, instintively thinking that WHERE will not work, BUT IT ACTUALLY DOES WORK TOO, as I've checked it a while after completing the task. (10 minutes)

- Fixed pagination in my Otodom scraper (scraping5-selenium-otodom) - description in Polish: Przekopiowałem fragmenty kodu dotyczące paginacji do oddzielnego pliku pagination.py. Loopowało mnie między stronami 1 i 2. Dość szybko okazało się, że problem wynikał z klikania przycisku do poprzedniej strony - pominąłem go w pierwszej chwili, bo pojawiał się dopiero od drugiej strony, ale miał taką samą klasę.
Najpierw przekombinowałem, ale najprostsze wydaje mi się ustawienie go jako ostatni przycisk [-1] - nie ma już innych przycisków o tej klasie, więc to fajnie działa.
Dodatkowo przy okazji ofc wywaliłem hardcodowaną liczbę current_page_number i podmieniłem ją po prostu za realną wartość z aktualnie aktywnego przycisku (ma odmienną klasę, fajnie)
Przy tej całej operacji pojawiły się też problemy z porównywaniem intów i stringów, bo na początku chwytałem przycisk current_page i wyciągałem z tego .text,
aby to sfixować, stworzyłem odmienną zmienną current_page_number, gdzie mamy po prostu int(blabla_chwytanie_przycisku.text) - nie wiem, czy da się prościej, ale imo jest spoko. (45 minutes)


26.10.2025 (Day 18, Sunday)
- I've created a local agent based on Claude, which will work as a Python tutor for me now. 
I absolutely fell in love with the SQL learning technique and wanted to re-implement it for Python as well, in order to practice regularly and become a Python beast. I've created and already tested it for the first day and it works great! Will probably include more feedback soon. (1.5 hr)


27.10.25 (Day 19)
- Started this week with a SQL test from the previous week - I got 10/10 without much hesitation, that's a very good sign! (10 mins)
- Went through Lesson 4 of my SQL Course - JOINS and UNION operations - I've prepared extensive notes (1.5 hr)
- Finished sql exercises - couldn't finish the advanced exercise today as it required CTE and I've never used it before (45 mins)
- Completed day2 of learning Python with my private Claude Agent - I like how it works, today's session was pretty demanding and I've learned some useful things and reinforced the basics - The performance of the agent is clean overall - it makes some mistakes, AND REQUIRES CHECKING, but it's adjusting and reacting to my feedback. I'm pretty satisfied with its performance and I can definitely learn this way! (1 hr)
- Added a try-except->finally block in my Otodom scraper to handle error404, so we can continue scraping instead of interrupting the code (10 min)
- As for otodom scraper - I've also noticed some apartments are repeated because they're promoted and reappear on eveyr single page - we simply have to stick only to unique links in the end, and also adjust the format of everything to make sure it all works properly

28.10.25 (Day 20)
- SQL Course Exercises + additional UNION exercises - It all went pretty well, but I made an error in INTERSECT exercise, overengineering my solution slightly (1.5 hr)
- Struggled with a practice Interview question on Datalemur today - I properly worked out the JOIN and GROUP BY to get the correct unique queries for each employee in the specified period. However, the latter parts of the task were more difficult and required CTE, so I had to look it up eventually. I decided TO LEAVE IT FOR NOW - I've exhausted all of the current options I can use right now - I will return to it and solve it once I have the tools to do so. (1 hr)
- Finished another day of Python learning with my agent - got max points from all the 8 tasks (40 mins)
- Also built a Python mini-project for week1 - it didn't take too long and allowed me to ground my knowledge and learn a few useful things. I'm not yet sharing these in my career-log repo, but I might do so at some point! (1.5 hr)
- Followed up with some exercises from the ML course on lists & sets. I've created a new folder python-practice and a file exercises.py in this repo - it's not my only Python practice file, as the other one is in the other folder with my agent - perhaps I will also add exercises from there here.
(1.5 hr)

29.10.25 (Day 21)
- Started with a morning SQL session (1 hr)
- Followed up with an exercise from Datalemur - today's it was JPMorgan Chase Cards Issued Difference exercise - it wasn't too difficult, I've managed to finish it quickly using GROUP BY and aggregate functions - piece of cake, compared to yesterday (10 mins)
- Followed up with another session of Python with my teaching agent. Feeling like today it was even a bit too easy - a good sign toward the end of the week and I'm getting close to this week's exam, which will be an addi
tion to my learning session tomorrow. (1 hr)
- Followed up with Python exercises - included them in exercises.py (1 hr)

30.10.25 (Day 22)
- Started the day with my morning SQL routine - today the questions about JOIN and UNION seemed to be hard, but in the end I got a max score (1 hr)
- Followed up with another Datalemur Interview task - Alibaba Compressed Mean - I had to use SUM and then put everything in a subquery, divide and round the results. The issue was the ROUND function returned an error related to value types, despite having correct syntax. It was frustrating and I tried different approaches, but eventually I checked it and found out that it happens in Postgres and you have to use ::NUMERIC suffix - here it was: SELECT ROUND(total_items::NUMERIC / total_orders, 1) AS mean FROM... (30 mins)
- Finished another Python session with my agent - today's the last day before the weekly exam (40 mins)
- Python exercises with for loop and strings - I've enjoyed these and managed to do a lot of things on my own - there were some little things that I had to loop up. e.g - isalpha() or isupper()/islower() methods, but I was able to properly create a valid logic before that (1.5 hr)

31.10.25 (Day 23)
- Started the day with a long session with SQL - I've completed 2 additional modules on JOIN and types of JOIN + quite long exercises today - again with these JOINS I have a feeling of uncertainty when finishing and clicking "SUBMIT" and so it was today, but fortunately I got a max score again - NICE! (2 hr)
- Followed up with another Datalemur Interview task - CVS Health Pharmacy Analytics (P1) - it was a very easy task for me now - but I guess I'd struggle with it like 2-3 weeks ago (3 mins)
- Finished the weekly Python exam with my teacher agent - it went very smoothly and I've got 96% out of it - corrected to 100% after pointing out that the question was ambiguous and I've also given a correct answer, as there were two correct answers (20 mins)

3.11.25 (Day  24)
- Started this week with a SQL test from the last week - got 13/15 points (pretty nice!)(15 mins)
- Followed up with another weekly lesson of SQL - this week we will be focusing on CTE expressions in SQL - I paused the video a few times and took notes as always (1.5 hr)
- Completed today's set of SQL exercises - got max points and I must admit using CTE is very satisfying and also kinda natural for me now - I guess it's because I've dont a lot of practice of all the functions and syntax during the past weeks and CTE is basically all about wrapping these things into little blocks and combining them - good stuff (45 mins)
- Completed another Datalemur exercise - CVS Health Pharmacy Analytics (P2) - it wasn't too difficult with the use of CTE, and it seems I've unlocked a new level (10 mins)