from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


from bs4 import BeautifulSoup

opt = Options()

opt.add_argument("--headless")


def getJobsRemoteOk():

    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=1).install(),chrome_options=opt)
    driver.get('https://remoteok.com/')

    # html = driver.page_source

    # soup = BeautifulSoup(html,"lxml")
    #job-107986 #jobsboard > tbody > tr.job.job-107986.verified.new.has-highlight-color.sticky.dark.\=\#0038ff\=
    # jobs =  soup.select("#jobsboard > tbody > tr.job")
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.querySelector('#jobsboard').scrollHeight")

    pull_jobs = []

    index,size = 0, 100

    while True:
        html = driver.page_source

        driver.execute_script("window.scrollTo(0, document.querySelector('#jobsboard').scrollHeight);")

        soup = BeautifulSoup(html,"lxml")

        jobs =  soup.select("#jobsboard > tbody > tr.job")

        pull_jobs = jobs

        # Scroll down to bottom
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.querySelector('#jobsboard').scrollHeight")
       
        if  last_height>= 164636 or len(pull_jobs) >= 1500:
            break
        last_height = new_height
        index += 100
        size += 100
        scraped_jobs = []

    for job in jobs:
        data = {}
    
        image_col = job.select_one("td.image.has-logo")

        location_salary = job.select("td.company.position.company_and_position > div.location")

        if len(location_salary) == 2:
            location = location_salary[0]
            salary = location_salary[1]
        elif len(location_salary) == 1:
            if location_salary[0].text.strip().startswith("💰"):
                salary = location_salary[0]
                location=None
            else:
                location = location_salary[0]
                salary=None
        else:
            location = None
            salary = None
        tags_col = job.select("td.tags > a")
        company_name = job.select_one("td.company.position.company_and_position > span.companyLink > h3")
        position = job.select_one("td.company.position.company_and_position > a > h2")
        created_at = job.select_one("td.time > a > time")
        tags = []
        apply_url = job.select_one("td.source > a")

        if image_col:
            logo_src = image_col.select_one('a').find("img")["src"]
            
        else:
            logo_src = None

        for tag in tags_col:
            tag_name = tag.select_one("div > h3")

            tags.append(tag_name.text.replace("\t", "").replace("\r", "").replace("\n", ""))

        data.setdefault("logo",logo_src) 
        data.setdefault("Company Name",company_name.text.strip())
        data.setdefault("Position", position.text.strip())
        if location:
            data.setdefault("location",location.text.replace("🌏","").replace("🇺🇸",""))
        if salary:
            data.setdefault("salary",salary.text.replace("💰",""))
        data.setdefault("tags",tags)
        data.setdefault("created_at",created_at["datetime"])
        data.setdefault("apply_url","https://remoteok.com"+apply_url["href"])
        data.setdefault("scraped_from", "remoteok")

        scraped_jobs.append(data)



    print("Done Scrapping RemoteOk....")

    driver.quit()
    return scraped_jobs
