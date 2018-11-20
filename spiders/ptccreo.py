'''
Created on 10/11/2018 By K'Ron Simmons

'''
import datetime
from selenium import webdriver
import unicodecsv
from tqdm import tqdm


# After the entire page is expanded, we grab all of the links
def initiate():
    driver.set_page_load_timeout(10)
    search_openings = driver.find_element_by_id("srchOpenLink")  # first search button on first page
    search_openings.click()
    driver.set_page_load_timeout(10)
    submit = driver.find_element_by_name("submit1")  # second search button on second page
    submit.click()


def get_links():
    # the tag name on each ID is different but they all begin with "viewjobdetails" and end with some number. We use a regular expression to match each case
    job_url = driver.find_elements_by_css_selector(
        "a[id^=viewjobdetails]")
    a = []
    for l in job_url:
        href = l.get_attribute("href")
        a.append(href)  # adding the links to list 'a'
    return a  # returning that list as the function


def get_dates():
    job_date = driver.find_elements_by_css_selector(
        'td[id$="_7"]')  # all of the IDs for the dates end with _7. used regex to find them
    b = []

    for i in job_date:
        text = i.text  # getting the text of that date
        b.append(text)  # adding that text to list 'b'
    return b


def get_hire_type():
    job_type = driver.find_elements_by_css_selector(
        'td[id$="_5"]')  # all of the IDs for the hire type end with _5. used regex to find them
    c = []

    for i in job_type:
        text = i.text
        c.append(text)
    return c

# Now we visit each page
def go_to(href):
    driver.set_page_load_timeout(10)  # allowing the page to load before we begin to scrape
    driver.get(href)


# on each page, we grab the title, Job ID, Location, Category, Hire type, and Requirements.
def get_title():
    title = driver.find_element_by_id("Business Title")
    return title.text


def get_job_id():
    # used XPATHS to avoid grabbing data with same generic "names" attributes in the HTML. These are very specific to what we want
    id = driver.find_element_by_xpath(
        '//*[@id="Job Req Number"]')
    return id.text


def get_location():
    location = driver.find_element_by_id("Country-City")
    return location.text


def get_category():
    category = driver.find_element_by_xpath('//*[@id="PTC Org"]')
    return category.text


def get_requirements():
    requirements = driver.find_element_by_xpath('//*[@id="Job Description for Advertising Purposes"]')
    return requirements.text


def get_benefits():
    try:
        benefits = driver.find_element_by_xpath('//*[@id="Why Join Us and Benefits Summary"]')
        return benefits.text
    except Exception:
        return "None "


if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day
    company = "Dassault"  # The companies name

    driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
    # driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30)  # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-PTCCreo.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-PTCCreo.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Job Description and Requirements", "Job Benefits", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        driver.get("https://careers.ptc.com/")
        driver.implicitly_wait(5)  # allows the page to load its elements dynamically
        initiate()  # clicking the two submit buttons of first two pages
        driver.implicitly_wait(5)

        # list of links to crawl
        hire_type_list = []
        # List of the hire type
        urls_list = []
        # list of the dates
        dates_list = []

        numbers = driver.find_element_by_xpath('//*[@id="yui-pg0-0-pages"]')
        numbers = numbers.find_elements_by_class_name('yui-pg-page')  # the amount of pages we need to click through
        numbers = (len(numbers))  # This is how many times we need to click the next button

        i = 1
        print("Collecting Jobs to be scraped...")
        while i <= numbers:  # although the amount of pages is n, we can only click n-1 times through the pages
            # loop through each page and append the info its respective list above
            hire_type_list.extend(get_hire_type())
            urls_list.extend(get_links())  # setting the list of links to var urls
            dates_list.extend(get_dates())  # setting the list of dates to var date

            # for the last page, try and find the next page button...
            try:
                next_page = driver.find_element_by_id(
                    'yui-pg0-0-next-link')
                next_page.click()
                driver.implicitly_wait(5)  # allowing the page to load a bit

            # if we click on a button thats not there, it throws an exception so we just accept the error and go on.
            except Exception:
                pass
            i += 1

        dictionary = (tuple(zip(urls_list, hire_type_list,
                                dates_list)))  # combining the three lists of Links, dates, and hire types because theyre on the same page

        print("Scraping Job Info...")
        for k, v, e in tqdm(dictionary):  # this is the structure of the tuple... (url, hire_type, date_list)
            url = k
            hire_type = v
            posting_date = e

            go_to(url)
            company = "PTCCreo"
            title = get_title()
            req_number = get_job_id()
            country = get_location()
            category = get_category()
            requirements = get_requirements()
            benefits = get_benefits()

            list = [date, company, req_number, category, country, title, hire_type, posting_date, requirements,
                    benefits, url]  # order of the information in the csv file. Can be moved around
            wr.writerow(list)  # Writing the information gathered to the file one line at a time
            del list

    print("Done")
    driver.quit()  # Closing the driver
    myfile.close()  # closing the file
