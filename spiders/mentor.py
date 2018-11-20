'''
Created on 10/19/2018 By K'Ron Simmons
'''

import datetime
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import unicodecsv
from tqdm import tqdm
from time import sleep

def get_links():
    a = []
    links = driver.find_elements_by_class_name('oracletaleocwsv2-head-title')
    for l in links:
        href = l.find_element_by_tag_name('a')
        href = href.get_attribute('href')
        a.append(href)
    return a


if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day

    driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
    # driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
    driver.set_page_load_timeout(30)  # response time out of page in seconds. If the page takes too long, increase time
    print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-Mentor.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Mentor.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8', delimiter=',')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type"
                  , "Posting Date", "Job Description and Requirements", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        driver.get('https://chc.tbe.taleo.net/chc01/ats/careers/v2/searchResults?org=MENTOR&cws=44')
        driver.set_page_load_timeout(15)

        test = driver.find_element_by_class_name('oracletaleocwsv2-panel-number').text
        test = int(test) / 10

        i = 1
        while i <= test:
            driver.implicitly_wait(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            i += 1

        links_list = get_links()
        driver.quit()


        print("Collecting Link info")
        for url in tqdm(links_list):
            response = requests.get(url)  #requests each individal url
            soup = BeautifulSoup(response.text, "html.parser")  #parsing it into something useful
            a = soup.find(class_="col-xs-12 col-sm-12 col-md-4")  # finding the information by class name
            b = a.find_all('strong')  # drilling down and finding that info by its tags
            title = b[0].text
            country = b[1].text
            req_number = b[2].text
            category = b[3].text
            hire_type = "None"
            posting_date = "None"
            company = "Mentor Graphics"

            description = soup.find(class_='col-xs-12 col-sm-12 col-md-8').text[590:-85]  # slicing off unnecessary info from the front and back


            list = [date, company, req_number, category, country, title, hire_type, posting_date, description,
                    url]  # order of the information in the csv file. Can be moved around

            wr.writerow(list)  # Writing the information gathered to the file one line at a time
            del list

    myfile.close()  # closing the file
    print("Done!")
