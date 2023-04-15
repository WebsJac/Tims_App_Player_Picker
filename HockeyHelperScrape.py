import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html')

current_page = 1
playerName = []

while True:
    try:
        next_button = driver.find_element_by_xpath(f"//a[@ga4-page='{current_page + 1}']")
        next_button.click()
        current_page = current_page + 1
        html_text = requests.get("https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html").text
        soup = BeautifulSoup(html_text, 'lxml')
        statTable = soup.find('table', id="statistics")
        statTableBody = statTable.find('tbody')
        playerRows = statTableBody.find_all('tr')
        for row in playerRows:
            playerName.append(row.find('a').text)
        time.sleep(1)
        print(len(playerName))
    except:
        break

