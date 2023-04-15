import requests
from bs4 import BeautifulSoup

#Use http://www.hockeychallengepicks.ca/ to decide who's available to be picked
html_text = requests.get("http://www.hockeychallengepicks.ca/").text
soup = BeautifulSoup(html_text, 'lxml')

player_name1 = [] #make arrays for names
player_name2 = []
player_name3 = []

pick1_data = soup.find('div', id = "pick-1", class_ = "pickContainer")
table1_rows = pick1_data.find_all('tr')
#print(len(table1_rows)) check to make sure its 15 rows
for row in table1_rows: #python knows its rows
    player_name1.append(row.find('a').text) #will find the anchor text for each player (their name)
pick2_data = soup.find('div', id = "pick-2", class_ = "pickContainer")
table2_rows = pick2_data.find_all('tr')
for row in table2_rows: #python knows its rows
    player_name2.append(row.find('a').text) #will find the anchor text for each player (their name)
pick3_data = soup.find('div', id = "pick-3", class_ = "pickContainer")
table3_rows = pick3_data.find_all('tr')
for row in table3_rows: #python knows its rows
    player_name3.append(row.find('a').text) #will find the anchor text for each player (their name)

html_text = requests.get("https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html").text
soup = BeautifulSoup(html_text, 'lxml')
current_page = '1'
playerName = []
playerTeam = []
playerPosition = []
playerGamePlayed = []
playerGoals = []
playerPoints = []
playerPIM = []
playerTOI = []
playerPPTOI =[]
playerPPG = []
playerPPP =[]
playerPPPPercentage = []
playerG60 = [] #goals per 60min
playerShots = []
playerShotPercentage = []

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
next_page = soup.find('div', id = "AjaxRefresh").find('div', class_="tabletop").find_all('a')[-1].get('ga4-page')










