from bs4 import BeautifulSoup
import requests

url = "https://www.espncricinfo.com/live-cricket-score"
to_scrape = requests.get(url)
soup = BeautifulSoup(to_scrape.content, 'html.parser')    

find_team_and_score = soup.find(class_= "ds-flex ds-flex-col ds-mt-2 ds-mb-2")
team_and_score = find_team_and_score.getText(separator=' ', strip=True)
find_status_of_match = soup.find(class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
status_of_match = find_status_of_match.getText(separator=' ', strip=True)
