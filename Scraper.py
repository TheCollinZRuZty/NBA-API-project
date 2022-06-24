import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
import pymysql

URL = "https://www.nba.com/celtics/stats"

def scraping(URL):
      features="html.parser"
      result = re.search('com/(.*)/stats', str(URL))
      team=str(result.group(1))
      print(team)
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
      list_1 = soup_formatted.split("\n")

      lenght=len(list_1)
      divided_len=(lenght // 16)
      new_list = []
      n = 16
      for start_index in range(0, len(list_1), n):
            new_list.extend(list_1[start_index:start_index+n])
            new_list.append(team)
      
      new_list.pop()
      new_list.pop()
      chunked_list = list()
      chunk_size = 17
      for i in range(0, len(new_list), chunk_size):
            chunked_list.append(new_list[i:i+chunk_size])
      chunked_list=str(chunked_list)

      chunked_list=chunked_list.replace('[','(')
      chunked_list=chunked_list.replace(']',')')
      chunked_list=chunked_list[1:-1]
      print(chunked_list)

def insert_DB(values):
      # To connect MySQL database
      conn = pymysql.connect(
            host='localhost',
            port=3306,
            user="root'@'localhost", 
            password = '',
            db='playerstats',
      )
      SQL='INSERT INTO players20212022 (PlayerName,Number,Postions,GamesPlayed,Points,FG,FGper,3Pper,FTper,OREB,DREB,REB,AST,STL,Turnover,PF,Team) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
      VAL=values
      cur = conn.cursor()
      cur.executemany(SQL, VAL)
      output = cur.fetchall()
      print(output)
      print(cur.rowcount, "was inserted.") 
      # To close the connection
      conn.close()  
      # mydb = mysql.connector.connect(
      #       host="192.168.1.225",
      #       user="root'@'localhost",
      #       password="Jutland1916!?",
      #       database="playerstats"
      #       )
      # SQL='INSERT INTO players20212022 (PlayerName,Number,Postions,GamesPlayed,Points,FG,FGper,3Pper,FTper,OREB,DREB,REB,AST,STL,Turnover,PF,Team) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
      # VAL=values
      # mycursor = mydb.cursor()
      # mycursor.executemany(SQL, VAL)
      # mydb.commit()
      # print(mycursor.rowcount, "was inserted.") 

def main():
      values=scraping('https://www.nba.com/celtics/stats')
      print(values)
      output=insert_DB(values)
      print(output)
      
if __name__ == "__main__":
      main()
