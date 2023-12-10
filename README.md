# bin-day
A repo for my personal project that uses web-scraping and automation to text me which bin day it is that week.

I used developer tools in Chrome to look at the website I want to scrape, and find the exact referal link to the data I need once I'd put in my address details. Currently I have that unique url saved in my programme, which is then scraped using Beautiful Soup. I then parse the data and use regex to find the dates of upcoming green and blue bin days, use python's datetime module to convert to useful data types, and then use some conditional logic to compare both and print the upcoming result.

TO-DO //
- use automation tools so the programme runs on a weekly basis
- use automation tools to text the result out
POTENTIAL TO EXPAND //
- use selenium to automate browser actions to interact with the dynamic elements on the page, so the start url can be less specific and can take different user data
- flask app for user interface
- set up a user database - postgreSQL?
- set up secure log-in