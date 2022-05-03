#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
import re
   
URL = "https://www.nba.com/sixers/stats"
r = requests.get(URL)
soup = BeautifulSoup(r.content)
soup=str(soup)

soup=soup.split('</tbody>',1)
soup=soup[0]
soup=soup.split('<tbody>',1)
soup=soup[1]

soup=str(re.sub(r'<tr>','<tr> \n',soup))
soup=str(re.sub(r'</tr>','</tr> \n',soup))
soup=str(re.sub(r'<th>','<th> \n',soup))
soup=str(re.sub(r'</th>','</th> \n',soup))
soup=str(re.sub(r'<td>','<td> \n',soup))
soup=str(re.sub(r'</td>','</td> \n',soup))
soup=str(re.sub(r'</tr>','',soup))
soup=str(re.sub(r'" class="player_name"',' \n',soup))
soup=str(re.sub(r'<th aria-label=','x',soup))
soup=str(re.sub(r'<td aria-label=','x',soup))
soup=str(re.sub(r'Games Played" class="gp" title=','"',soup))
soup=str(re.sub(r'Points" class="pts" title=','"',soup))
soup=str(re.sub(r'Field Goals Made" class="fgm" title=','"',soup))
soup=str(re.sub(r'Field goal %" class="fg_pct" title=','"',soup))
soup=str(re.sub(r'Three point %" class="fg3_pct" title=','"',soup))
soup=str(re.sub(r'Free throw %" class="ft_pct" title=','"',soup))
soup=str(re.sub(r'Offensive Rebounds" class="oreb" title=','"',soup))
soup=str(re.sub(r'Deffensive Rebounds" class="dreb" title=','"',soup))
soup=str(re.sub(r'Rebounds" class="reb" title=','"',soup))
soup=str(re.sub(r'Assists" class="ast" title=','"',soup))
soup=str(re.sub(r'Steals" class="stl" title=','"',soup))
soup=str(re.sub(r'Turn overs" class="tov" title=','"',soup))
soup=str(re.sub(r'Fouls" class="pf" title=','"',soup))
soup=str(re.sub(r' Games Played">','"',soup))
soup=str(re.sub(r' Points">','"',soup))
soup=str(re.sub(r' Field Goals Made">','"',soup))
soup=str(re.sub(r' Field goal %">','"',soup))
soup=str(re.sub(r' Three point %">','"',soup))
soup=str(re.sub(r' Free throw %">','"',soup))
soup=str(re.sub(r' Offensive Rebounds">','"',soup))
soup=str(re.sub(r' Deffensive Rebounds">','"',soup))
soup=str(re.sub(r' Rebounds">','"',soup))
soup=str(re.sub(r' Assists">','"',soup))
soup=str(re.sub(r' Steals">','"',soup))
soup=str(re.sub(r' Turn overs">','"',soup))
soup=str(re.sub(r' Fouls">','"',soup))
soup=str(re.sub(r'_blank',' \n',soup))
soup=str(re.sub(r'<td>','x 0',soup))
soup=str(re.sub(r'—</td>','',soup))
soup=str(re.sub(r'<tr no_striping="1" tabindex="0">x',' ',soup))
soup=str(re.sub('""[^>]+>', ' ', soup))
soup=str(re.sub(r't.+"','',soup))
soup=str(re.sub(r'">.+>','',soup))
soup=str(re.sub(r', ',' \n',soup))
soup=str(re.sub(r' "',' \n',soup))
soup=str(re.sub(r'Number ','',soup))
soup=str(re.sub(r'x"',' \n',soup))
soup=str(re.sub(r'x ',' \n',soup))

lines = soup.split("\n")
soup_lines = [line for line in lines if line.strip() != ""]
soup_formatted = ""
for line in soup_lines:
      soup_formatted += line + "\n"
print(soup_formatted)
