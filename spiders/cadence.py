'''
Created on 10/18/2018 By K'Ron Simmons
Selenium Lazy scroll -Cadence: https://cadence.wd1.myworkdayjobs.com/External_Careers

The web page doesnt have links!!! Getting creative...
Might not work as expected. If something out of the ordinaty happens, please contact me.

'''
import datetime
from selenium import webdriver
import unicodecsv
from tqdm import tqdm
import curlresources



if __name__ == '__main__':
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime(
        "%Y-%m-%d")  # formatting that date to Year - Month - Day

    print("In progress... Please wait. ")
    a = open("../CSVs/" + date + "-Jobs-Cadence.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Cadence.csv", "ab+") as myfile:  # opening a file to write the data to
        wr = unicodecsv.writer(myfile, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Job Description and Requirements","Posting URL"]
        wr.writerow(header)  # Writing a header line to the file

        url_list = []

        calls = [curlresources.first_call(),
                 curlresources.second_call(),
                 curlresources.third_call(),
                 curlresources.fourth_call(),
                 curlresources.fifth_call(),
                 curlresources.sixth_call(),
                 curlresources.seventh_call(),
                 curlresources.eight_call(),
                 curlresources.ninth_call(),
                 curlresources.tenth_call(),
                 ]

        print("Collecting Link info")
        for i in tqdm(calls):
            url_list.extend(i)

        driver = webdriver.Chrome("../Drivers/chromedriver.exe")  # location of .exe
        # driver.set_window_size(400, 400)  # px size of browser in window (w, h). Kept small to keep out of the way.
        driver.set_page_load_timeout(
            30)  # response time out of page in seconds. If the page takes too long, increase time
        print("Loading page now... If it doesn't load, check conncetion and relaunch the program.")

        print("Scraping Links")
        for url in tqdm(url_list):
            full_url = "https://cadence.wd1.myworkdayjobs.com" + url
            driver.get(full_url)
            driver.implicitly_wait(30)
            info = driver.find_elements_by_class_name("WMCO")

            company = "Cadence"
            category = "None"
            title = (info[2].text)
            country = (info[3].text)
            description = (info[4].text)
            posting_date = (info[5].text)
            hire_type = (info[6].text)
            req_number = (info[7].text)

            list = [date, company, req_number, category, country, title, hire_type, posting_date, description,
                    full_url]  # order of the information in the csv file. Can be moved around

            wr.writerow(list)  # Writing the information gathered to the file one line at a time
            del list

        driver.quit()

    myfile.close()  # closing the file
    print("Done!")
