'''
Created on 10/17/2018 By K'Ron Simmons

'''
import datetime
from selenium import webdriver
import unicodecsv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import json
from time import sleep


TAG_RE = re.compile(r'<[^>]+>')  # regular expression matching HTML mark up
def remove_tags(text):  # a function to remove the HTML from the description
    return TAG_RE.sub('', text)


def get_links():
    print("Collecting Jobs to be scraped...")
    a = []
    # the tag name on each ID is different but they all begin with "viewjobdetails" and end with some number. We use a regular expression to match each case
    job = driver.find_elements_by_class_name("jtable-data-row")
    for url in job:
        try:
            href = url.get_attribute("data-href")
            a.append(href)  # adding the links to list 'a'
        except Exception:
            print("skipped{}".format(url))
            pass
    return a  # returning that list as the function


def collect():  # strictly to collect the links
    print("Getting Links!")
    urls_list = []  # we need a list to hold all of the links
    test = True  # allows the loop to run until the condition changes
    while test == True:
        driver.set_page_load_timeout(15)  # allowing the page to load
        # loop through each page and append the info its respective list above
        urls_list.extend(get_links())  # setting the list of links to var urls
        sleep(1)
        amount = (len(urls_list))  # amount of links collected so far
        print("{} Jobs found so far".format(amount))  # gives us an update to the number of jobs being collected

        try:
            driver.implicitly_wait(15)  # the driver actually waits until the object is present
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")  # we need to scroll to the bottom of the page to click on the next button
            selector = "jtable-page-number-next-mobile"
            next_button = driver.find_element_by_class_name(selector)  # finding that next button
            driver.execute_script("arguments[0].setAttribute('class','ui-state-hover')",
                                  next_button)  # pretending to hover over the next button to activate it.
            driver.find_element_by_class_name("ui-state-hover").click()  # clicking the next button
        except Exception:
            # once that next button can no longer be clicked we can exit the loop
            print("Done collecting... ")
            driver.quit()
            test = False  # changing that above condition to false so that the loop stops

    total = (len(urls_list))
    print("Now scraping {} jobs".format(total))

    return urls_list  # returning this value to the method being called.



if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day

    driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
    # driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30)  # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-Ansys.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Ansys.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Posting Date","Job Description and Requirements","Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        driver.set_window_size(300,
                               800)  # opens the window wide enough to move elements and click on appropriate buttons
        driver.get("https://jobs.ansys.com/search/searchjobs")
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(15)
        # sleep()
        try:
            # theres an initial pop up we need to check for
            driver.find_element_by_class_name("cc-dismiss").click()
        except Exception:
            pass

        url_list = collect()  # a list of urls to visit

        for url in tqdm(url_list):
            response = requests.get(url)  # vsiting each page individually to grab info
            soup = BeautifulSoup(response.text, "html.parser")

            scripts = (soup.find_all("script"))

            string_information = scripts[12].text[25:-3]
            string_description = scripts[13].text[5:]

            description_data = json.loads(string_description)
            data = json.loads(string_information)  # loading the information as a proper JSON string to be parsed

            company = "Ansys"
            req_number = data["ReferenceNumberJson"]
            category = data["AtsCategoryNamesJson"]
            country = "{}, {} {}".format(data["LocationNamesJson"], data["AddressesDataJson"], data["ZipCodesJson"])
            title = data["TitleJson"]
            hire_type = data["TypeNameJson"]
            posting_date = data["PostedDateJson"]
            description = remove_tags(description_data["description"])

            list = [date, company, req_number, category, country, title, hire_type, posting_date, description,
                    url]  # order of the information in the csv file. Can be moved around

            wr.writerow(list)  # Writing the information gathered to the file one line at a time
            del list

    myfile.close()  # closing the file
    print("Done!")
