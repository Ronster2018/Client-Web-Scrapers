'''
Created on 9/13/2018 By K'Ron Simmons

A custom web scraper for Synopsys!!!

Scrapers like Beautiful Soup and Scrappy did not work because the site is Dynamically loaded. That just means it needs a
web page open to interpret the JS that loads the data. BS4 and Scrappy both make a request from the server but cannot
interpret the dynamic data. This was worked around with the use of the Selenium browser. This is a browser that can open
itself, load the page, and scrape the interpreted information.

Usage:
$ pip install -r requirements.txt
$ python synopsys.py

Check the same directory of the program for your output file of [date]-Jobs-Sysopsys.csv
May have to double-click the job description cell in excel to view the entire job description.
'''

import datetime
from selenium import webdriver
import time
import unicodecsv
from tqdm import tqdm

# The page that contains 900+ job postings needs to be expanded first. Its dynamically.
def open_pages():
    try:
        while driver.find_element_by_class_name("showMoreJobs").is_displayed() == True:  # checking to see if an element on the page exists or not.
            driver.find_element_by_class_name("showMoreJobs").click()  # while that element exists, we click to expand the page.
    except Exception as e:  # Since it does no return false when the element is no longer there, we catch the exception.
        pass  # after we catch the exception, the job is done.

# After the entire page is expanded, we grab all of the links
def get_links():
    print ("Collecting Jobs to be scraped...")
    urls = []
    jobs = driver.find_elements_by_class_name("jobtitle")  # Grabbing each job link.
    for job in tqdm(jobs):  # tqdm shows the progress bar in the console. Only works with loops
        href = job.get_attribute('href')
        urls.append(href)  # adding each link to a list.
    return urls  # returning that list as the function

# Now we visit each page
def go_to(href):
    driver.get(href)

# on each page, we grab the title, Job ID, Location, Category, Hire type, and Requirements.
def get_title():
    title = driver.find_element_by_class_name("jobtitleInJobDetails")
    return title.text

def get_job_id():
    id = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[2]/p') # used XPATHS to avoid grabbing data with same generic "names" attributes in the HTML. These are very specific to what we want
    return id.text

def get_location():
    location = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[3]/p')
    return location.text

def get_category():
    category = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[5]/p[2]')
    return category.text

def get_hire_type():
    hire = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[6]/p[2]')
    return hire.text

def get_requirements():
    requirements = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[4]')
    return requirements.text


if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime("%Y-%m-%d")   # formatting that date to Year - Month - Day
    company = "Synopsys" # The companies name

    driver = webdriver.Chrome("Libraries/chromedriver.exe") # location of .exe
    driver.set_window_size(400, 300)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30) # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")
    driver.get("https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=25235&siteid=5359#home")
    driver.find_element_by_class_name("primaryButton").click()  # clicking on the search button to reveal all jobs
    time.sleep(5)  # giving the page time to load
    print ("In progress... Please wait. ")
    a = open(date+"-Jobs-Synopsys.csv", "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  #closing it with nothing in it.
    with open(date+"-Jobs-Synopsys.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel', encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Date", "Company", "Business Title", "Job ID", "Hiring Location", "Job Category", "Hire Type", "Job Description and Requirements", "URL"]
        wr.writerow(header)  # Writing a header line to the file

        open_pages()  # calling the open pages function to open the entire page first
        urls = get_links()  # setting that list to var urls
        total = len(urls)  # Total amount of "jobs" to be scraped
        print ("Total Jobs to scrape: "+ str(total))
        print ("Scraping Job Info...")
        for sites in tqdm(urls, dynamic_ncols=True):  # urls = get_links(). Dynamic_ncols just allows the progress bar to grow and shrink with the terminal window.
            go_to(sites)
            title = get_title()
            id = get_job_id()
            location = get_location()
            category = get_category()
            hire_type = get_hire_type()
            requirements = get_requirements()
            url = sites
            list = [date, company, title, id, location, category, hire_type, requirements, url]  # order of the information in the csv file. Can be moved around
            wr.writerow(list)
            del list
    driver.quit()  # Closing the driver
    myfile.close()  # closing the file