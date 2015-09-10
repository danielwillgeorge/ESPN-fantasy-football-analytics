import pandas as pd
import requests
from bs4 import BeautifulSoup

# @Author Daniel George
# @Works Cited: Daniel Rodriguez, https://github.com/danielfrg/nba

url = "http://espn.go.com/nfl/teams"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
tables = soup.find_all("ul", {"class":"medium-logos"})

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []
for table in tables:
  lis = table.find_all("li")
  for li in lis:
    info = li.h5.a
    teams.append(info.text)
    url = info["href"]
    teams_urls.append(url)
    prefix_1.append(url.split("/")[-2])
    prefix_2.append(url.split("/")[-1])


dic = {"url": teams_urls, "prefix_2": prefix_2, "prefix_1": prefix_1}
teams = pd.DataFrame(dic, index=teams)
teams.index.name = "team"
teams.to_csv("teams.csv")

#for index, row in teams.iterrows():
#    url = row['url']
#    print index, url