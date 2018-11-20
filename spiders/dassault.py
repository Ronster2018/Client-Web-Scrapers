'''
Created on 10/13/2018 By K'Ron Simmons

'''
import datetime
from selenium import webdriver
import unicodecsv
from tqdm import tqdm


# After the entire page is expanded, we grab all of the links
def get_links():
    try:
        # a button to accept cookies appears sometimes. We need to dismiss it to continue
        if driver.find_element_by_id("popin_tc_privacy_button").is_displayed() == True:  # check for button
            driver.find_element_by_id("popin_tc_privacy_button").click()  # click to dismiss button
        else:
            pass
    except Exception:  # if not present, we get an error.
        pass  # ignore the error and carry on
    urls = []  # creating a list of URLS to crawl
    job_block = driver.find_element_by_id("woc-cards-5ac33e215a742")  # Grabbing each job link.
    jobs = job_block.find_elements_by_xpath('.// div / div / article / a')
    for job in jobs:  # tqdm shows the progress bar in the console. Only works with loops
        href = job.get_attribute("href")
        urls.append(href)  # adding each link to a list.
    return urls  # returning that list as the function


# Now we visit each page
def go_to(href):
    driver.set_page_load_timeout(10)  # allowing the page to load before we begin to scrape
    driver.get(href)

# on each page, we grab the title, Job ID, Location, Category, Hire type, and Requirements.
def get_title():
    title = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[2]/h1")
    return title.text

def get_job_id():
    id = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[1]/div[1]/ul/li[4]")  # used XPATHS to avoid grabbing data with same generic "names" attributes in the HTML. These are very specific to what we want
    return id.text

def get_location():
    location = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/ul/li[1]")
    return location.text


def get_category():
    category = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/ul/li[3]")
    return category.text


def get_hire_type():
    hire = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/ul/li[2]")
    return hire.text


def get_requirements():
    requirements = driver.find_element_by_class_name("job-wrapper_body")
    return requirements.text


if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day
    company = "Dassault"  # The companies name

    driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
    driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30)  # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-Dassault.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Dassault.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Job Description and Requirements", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        # Initiate the loop
        url_list = []
        driver.get('https://careers.3ds.com/jobs')
        driver.implicitly_wait(5)
        limit = driver.find_element_by_css_selector("#woc-pager-5ac33e215a742 > div > ul > li.ds-pagination__goto.is-boundary")  # the number of the last page
        limit = limit.find_element_by_tag_name('a').text
        limit = int(limit)  # converting that string to a number
        print("Browsing pages and collecting links...")
        for i in tqdm(range(2)):  # goes throguh this loop "limit" amount of times
            driver.get("https://careers.3ds.com/jobs?wocset={}".format(i))
            driver.implicitly_wait(5)  # allows the page to load its elements dynamically
            urls = get_links()  # setting that list to var urls
            url_list.extend(urls)
            # total = len(urls)  # Total amount of "jobs" to be scraped
            # print("Total Jobs to scrape: " + str(total))

        print("Now scraping {} jobs".format(len(url_list)))
        for sites in tqdm(url_list,
                          dynamic_ncols=True):  # urls = get_links(). Dynamic_ncols just allows the progress bar to grow and shrink with the terminal window.
            go_to(sites)
            company = "Dassault"
            posting_date = ""
            title = get_title()
            req_number = get_job_id()
            country = get_location()
            category = get_category()
            hire_type = get_hire_type()
            requirements = get_requirements()
            url = sites
            list = [date, company, req_number, category, country, title, hire_type, posting_date,
                    requirements,
                    url]  # order of the information in the csv file. Can be moved around
            wr.writerow(list)
            del list

    print("Done")
    driver.quit()  # Closing the driver
    myfile.close()  # closing the file
