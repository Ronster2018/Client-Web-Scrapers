'''
Created on 10/16/2018 By K'Ron Simmons
https://www.altium.com/careers/positions Besutiful Soup!
'''

from bs4 import BeautifulSoup
import requests
import datetime
import unicodecsv
from tqdm import tqdm


def get_date(new_soup):  # new soup is the new page that we get. Here we are getting the posting date of the pages
    date = new_soup.find(class_="posted-text")
    return date.get_text()


def get_req_number():
    var = "None found"
    return var


def get_job_category():
    var = "None found"
    return var


def get_title_and_location(new_soup):
    title = new_soup.find("h3")
    return title.get_text()


def get_hire_type():
    var = "None found"
    return var


def get_job_deets(new_soup):
    job = new_soup.find(class_="responsibilities")
    requirements = new_soup.find(class_="requirements")
    job_deets = "{} {}".format(job.get_text(), requirements.get_text())
    return job_deets


if __name__ == "__main__":
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime("%m-%d-%Y")  # formatting that date to Month - Day- Year
    a = open("../CSVs/" + date + "-Jobs-Altium.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Altium.csv", "ab+") as file:  # opening the CSV file to be written to
        wr = unicodecsv.writer(file, dialect='excel',
                               encoding='utf-8',delimiter = ",")  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Posting Date", "Job Description and Requirements", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file

        start_url = "https://www.altium.com/careers/positions"  # since the first page will go p, we will be passing it a new number each time
        page = requests.get(start_url)  # requesting initial home page
        soup = BeautifulSoup(page.text, 'html.parser')  # parsing that home page into something readable

        print("Collecting info and scraping...")
        for lists in tqdm(soup.find_all(class_="views-field-title-1")):  # Finding all of the links on the first page
            url = lists.find_all('a')
            for i in url:
                end_url = (i.get("href"))  # the site contains relative links like /location/job/stuff.html
                full_url = ("https://www.altium.com{}".format(
                    end_url))  # we need to concationate the beginning url with the relative one.
                page = requests.get(full_url)  # requesting that new page
                new_soup = BeautifulSoup(page.text, 'html.parser')

                posting_date = get_date(new_soup)
                temp = get_title_and_location(new_soup)
                title, country = temp.split(
                    "-")  # since this info is in the same line, we can split it by the "-" into two cariables, title and country
                scrape_date = date
                company = "Altium"
                req_number = get_req_number()
                job_category = get_job_category()
                description = get_job_deets(new_soup)
                hire_type = get_hire_type()

                # Adding above values to a list
                job = [scrape_date,
                       company,
                       req_number,
                       job_category,
                       country,
                       title,
                       hire_type,
                       posting_date,
                       description,
                       full_url]  # order of the information in the csv file. Can be moved around

                # Writing the List to a CSV file to be inported to Excel
                wr.writerow(job)
                del job
    file.close()
