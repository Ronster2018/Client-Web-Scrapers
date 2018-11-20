'''
Created on 10/17/2018 By K'Ron Simmons

'''
import datetime
from selenium import webdriver
import unicodecsv
from tqdm import tqdm
from time import sleep

def get_links():
    a = []
    # the tag name on each ID is different but they all begin with "viewjobdetails" and end with some number. We use a regular expression to match each case
    job = driver.find_elements_by_class_name("multiline-data-container")
    for url in job:
        links = url.find_element_by_tag_name("a")
        href = links.get_attribute("href")
        a.append(href)  # adding the links to list 'a'
    return a  # returning that list as the function


def get_dates():
    a = []
    job = driver.find_elements_by_css_selector('div.multiline-data-container > div:nth-child(3)')
    for i in job:
        dates = i.text
        a.append(dates)  # adding the links to list 'a'
    return a  # returning that list as the function


def get_ids():
    a = []
    job = driver.find_elements_by_css_selector('div.multiline-data-container > div:nth-child(4)')
    for i in job:
        ids = i.text
        a.append(ids)  # adding the links to list 'a'
    return a  # returning that list as the function


def get_location():
    a = []
    job = driver.find_elements_by_css_selector("div.multiline-data-container > div:nth-child(2)")
    for i in job:
        locations = i.text
        a.append(locations)  # adding the links to list 'a'
    return a  # returning that list as the function


def collect():  # strictly to collect the links
    print("Getting Links!")
    urls_list = []  # we need a list to hold all of the links
    date_list = []
    id_lists = []
    location_list = []
    test = True  # allows the loop to run until the condition changes
    i = 2  # 2 is the next page we want to click on. Cant click 1 because were already there.
    while test == True:
        driver.set_page_load_timeout(15)  # allowing the page to load
        # loop through each page and append the info its respective list above
        urls_list.extend(get_links())  # setting the list of links to var urls
        date_list.extend(get_dates())
        id_lists.extend(get_ids())
        location_list.extend(get_location())
        amount = (len(urls_list))  # amount of links collected so fat
        print("{} Jobs found so far".format(amount))  # gives us an update to the number of jobs being collected

        try:
            driver.set_page_load_timeout(15)  # allowing the page to load
            driver.implicitly_wait(5)  # the driver actually waits until the object is present
            next_button = driver.find_element_by_link_text(str(i))  # finding that next button
            next_button.click()
            sleep(2)
            i += 1
        except Exception:
            print("Done  Collecting Links! ")
            test = False
        # once that next button can no longer be clicked we can exit the loop

    all_list = tuple(zip(urls_list, date_list, id_lists, location_list))

    total = (len(urls_list))
    print("Now scraping {} jobs".format(total))

    return all_list  # returning this value to the method being called.


if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day

    driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
    # driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30)  # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-Autodeak.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Autodeak.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Job Description and Requirements", "Job Benefits", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        driver.set_window_size(300,
                               800)  # opens the window wide enough to move elements and click on appropriate buttons
        driver.get("https://autodesk.taleo.net/careersection/adsk_gen/jobsearch.ftl")
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(15)
        # sleep()

        all_list = collect()

        for u, d, i, l in tqdm(all_list):
            try:
                url = u
                driver.get(url)
                driver.implicitly_wait(10)
                posting_date = d
                req_number = i
                country = l
                company = "Autodesk"
                category = "None"
                hire_type = "Full - Time"  # These all seem to be full time jobs

                title = driver.find_element_by_id('requisitionDescriptionInterface.reqTitleLinkAction.row1').text
                description = driver.find_element_by_id('requisitionDescriptionInterface.ID1522.row1').text

                list = [date, company, req_number, category, country, title, hire_type, posting_date, description,
                        url]  # order of the information in the csv file. Can be moved around

                wr.writerow(list)  # Writing the information gathered to the file one line at a time
                del list
            except Exception:
                print("Job not available... moving on")
                pass
        driver.quit()

    myfile.close()  # closing the file
    print("Done!")
