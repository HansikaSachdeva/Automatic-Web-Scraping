# Automatic-Web-Scraping

The code scrapes the Name, Description, and Price of products using BeautifulSoup. 
The data is saved in a csv file automatically every four hours. 
The file is named as test-timestamp.csv

Using BeautifulSoup, a request is made to the website. 
The elements are stored in an empty list.
The csv file is created, and the name, description and price of products is written in it. 

BlockingScheduler is used to repeat this command every 4 hours. 

## Instructions to run

- Pre-requisites:

  - BeautifulSoup
  - BlockingScheduler 
```
pip install beautifulsoup4
pip install apscheduler
 ```

```
Terminal Commands
cd <Directory>
filename.py
```
