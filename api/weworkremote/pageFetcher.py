from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import cssutils
import os

from bs4 import BeautifulSoup

opt = Options()


opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--no-sandbox")
 



def getjobsWeWorkRemotely():
    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=1).install(),chrome_options=opt)
    driver.get('https://weworkremotely.com/')

    html = driver.page_source

    soup = BeautifulSoup(html,"lxml")

    jobs = soup.select("section > article > ul > li:not(.view-all)")
    scraped_jobs = []

    for job in jobs[:100]:
        data = {}
        logo_col = job.select_one("a > .flag-logo")

        if logo_col:
            logo_style = cssutils.parseStyle(logo_col["style"])

            logo_src = logo_style['background-image'].replace('url(', '').replace(')', '')
        else:
            logo_src = None

        company_name = job.select_one("a > .company")
        position = job.select_one("a > .title")
        location = job.select_one("a > span.region")
        if location:
            location = location.text.strip()
        salary = None
        created_at = job.select_one("a > .date > time")
        if created_at:
            created_at = created_at["datetime"]

        apply_url = job.select("a")[1]

        data.setdefault("logo",logo_src) 
        data.setdefault("Company Name",company_name.text.strip())
        data.setdefault("Position:", position.text.strip())
        data.setdefault("location",location)
        data.setdefault("salary",salary)
        data.setdefault("created_at",created_at)
        data.setdefault("apply_url","https://weworkremotely.com"+apply_url["href"])
        data.setdefault("scraped_from", "weworkremotely")

        scraped_jobs.append(data)
    driver.quit()

    print("Done Scrapping WeWorkRemotely....")

    return scraped_jobs
