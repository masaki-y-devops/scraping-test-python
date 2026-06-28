## Prerequisites
## PS> sudo winget install python.python.3.9
## then, restart terminal once
## PS> python -m pip install --upgrade pip
## PS> python -m pip install selenium
## PS> python -m pip install lxml

## Import modules
from time import sleep
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lxml import html

## Set headless mode
config = Options()
config.add_argument("--headless")
config.add_argument("--window-size=1920x1080")
user_agent = 'MyBot/1.0'   ## Declare myself as scraping bot explicitly for compliance
config.add_argument('user-agent={0}'.format(user_agent))

## Launch headless Chrome WebDriver and open target (scraping-friendly) website
driver = webdriver.Chrome(options=config)
driver.get("https://quotes.toscrape.com/")

## Wait for contents
sleep(5)

## Get entire page sources to pass it to lxml for JavaScript-enabled sites
entire_src = driver.page_source

## Extract page elements using XPath
src_for_lxml = html.fromstring(entire_src)
tgt_elem = src_for_lxml.xpath("//span[contains(@class,'text') and contains(@itemprop, 'text')]")

print("Displaying fetched elements...")
print("")
print(tgt_elem)

print("")
sleep(5)

## Print targeted results
print("Displaying targeted contents...")
print("")
for e in tgt_elem:
    all_lists = e.text_content()
    print(all_lists)

    '''
    ## Extract tests
    for line in all_lists.splitlines():
        if re.search('you|miracle|thinking|better', line):
            print("Displaying results that contain specific words...")
            print(line.strip())
    '''

'''
## Get element using xpath (tested but not working)
elem = driver.find_element(By.XPATH, "//span[contains(@class,'text') and contains(@itemprop, 'text')]")
print(elem.text)
'''

print("")
print("Displaying results are completed. Waiting...")
print("You can exit this script to press Ctrl+C.")

## Sleep in order to check results
sleep(10000)

## Close browser
driver.quit()