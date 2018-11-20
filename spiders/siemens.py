'''
Created on 10/9/2018 By K'Ron Simmons

'''

from bs4 import BeautifulSoup
import requests
import json
import datetime
import re
import unicodecsv
from tqdm import tqdm

TAG_RE = re.compile(r'<[^>]+>')  # regular expression matching HTML mark up
def remove_tags(text):  # a function to remove the HTML from the description
    return TAG_RE.sub('', text)


if __name__ == "__main__":
    now = datetime.datetime.now()  # getting the date at this very moment down to the seconds
    date = now.strftime("%m-%d-%Y")  # formatting that date to Month - Day- Year
    a = open("../CSVs/" + date + "-Jobs-Siemens.csv",
             "w+")  # creating and writing nothing to it. (deleting the contents)
    a.close()  # closing it with nothing in it.
    with open("../CSVs/" + date + "-Jobs-Siemens.csv", "ab+") as file:  # opening the CSV file to be written to
        wr = unicodecsv.writer(file, dialect='excel',
                               encoding='utf-8')  # Since were grabing it from the web, it has to be encoded in UTF-8
        header = ["Scrape Date", "Company", "Requisition Number", "Job Category", "Country", "Title", "Hire Type",
                  "Posting Date", "Job Description and Requirements", "Posting URL"]
        wr.writerow(header)  # Writing a header line to the file
        x = 500  # last page that results show up on
        print("Collecting Jobs!! Please wait")
        for i in tqdm(range(x), dynamic_ncols=True):
            try:
                url = "https://jobs.siemens-info.com/jobs?page={}".format(
                    i)  # since the first page will go p, we will be passing it a new number each time
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
                script = soup.find_all('script')  # lucky for us, a script loads all of the Job data we need.
                scripts = (len(script))
                for i in range(scripts):
                    try:
                        string = script[i].text[
                                 15:-2]  # Grabing that Job data and cutting off the beginning script tag and end bits
                        data = json.loads(string)  # loading the information as a proper JSON string to be parsed
                        for item in data:  # for each job in the chunk of "data", display information
                            for k, v in item.items():  # the data is broken up into dict key, value pairs
                                scrape_date = date
                                company = "Siemens"
                                req_number = (v["slug"])
                                job_category = (v["category"])
                                city = (v["city"])
                                state = (v["state"])
                                country = (v["country"])
                                country_code = (v["country_code"])
                                title = (v["title"])
                                posting_date = (v["posted_date"])
                                description = (v["description"])
                                description = remove_tags(description)
                                meta_data = (v['meta_data'])
                                job_url = meta_data.get("canonical_url")

                                # Adding above values to a list
                                job = [scrape_date,
                                       company,
                                       req_number,
                                       job_category,
                                       city + ", " + state + ", " + country + " " + country_code,
                                       title,
                                       posting_date,
                                       description,
                                       job_url]  # order of the information in the csv file. Can be moved around

                                # Writing the List to a CSV file to be inported to Excel
                                wr.writerow(job)
                                del job
                    except Exception:
                        pass
            except Exception:
                print("Skipping bad link")
                pass
        print("Done")
    file.close()
