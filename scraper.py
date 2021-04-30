#importing 
import requests
from bs4 import BeautifulSoup
import csv
import datetime

#function to repeat command at a given interval
def write_excel():
    # Make a request
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Create all_products as empty list
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()

        all_products.append({
        "Name": name,
        "Description": description,
        "Price": price,
        })

        #keys of the dictionary 
        keys = all_products[0].keys()

        #creating the csv file
        now = datetime.datetime.now()
        mydate = now.strftime('%Y%b%d')
        mytime = now.strftime('%H%M%S')

        csvName = 'test-'+mydate+''+mytime+".csv"

        #writing into csv file
        with open(csvName, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_products)

#using BlockingScheduler to repeat the command
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(write_excel, 'interval', hours=4)
scheduler.start()
