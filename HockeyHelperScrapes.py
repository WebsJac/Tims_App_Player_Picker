import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html')

current_page = 1
playerName = []

html_text = requests.get("https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html").text
soup = BeautifulSoup(html_text, 'lxml')
current_page = '1'

# ----------------------------------MAKE ARRAYS TO HOLD ALL THE VARIABLES---------------------------------------------
playerName, playerTeam, playerPosition, playerGamePlayed = [], [], [], []
playerGoals, playerPoints, playerPIM, playerPPG, playerPPP = [], [], [], [], []
playerTOI, playerPPTOI, playerPPPercentage = [], [], []
playerG60 = [] #goals per 60min
playerShots, playerShotPercentage = [], []

statTable = soup.find('table', id="statistics")
statTableBody = statTable.find('tbody')
playerRows = statTableBody.find_all('tr')
for row in playerRows:
    playerName.append(row.find('a').text)
    statColumn = row.find_all('td')
    playerTeam.append(statColumn[0].text)
    playerPosition.append(statColumn[2].text)
    playerGamePlayed.append(statColumn[3].text)
    playerGoals.append(statColumn[4].text)
    playerPoints.append(statColumn[6].text)
    playerPIM.append(statColumn[7].text)
    playerTOI.append(statColumn[9].text)
    playerPPTOI.append(statColumn[11].text)
    playerPPG.append(statColumn[14].text)
    playerPPP.append(statColumn[24].text)
    playerPPPPercentage.append(statColumn[28].text)
    playerG60.append(statColumn[29].text)
    playerShots.append(statColumn[41].text)
    playerShotPercentage.append(statColumn[42].text)

while True:
    try:
        next_page = current_page + 1
        next_button = driver.find_element_by_xpath('//a[@ga4-page="' + str(next_page) + '"]')
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

