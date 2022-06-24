CREATE TABLE players20212022 (
            PlayerName varchar(255) NOT NULL,
            Number varchar(255) NOT NULL,
            Postions varchar(255) NOT NULL,
            GamesPlayed varchar(255) NOT NULL,
            Points varchar(255) NOT NULL,
            FG varchar(255) NOT NULL,
            FGper varchar(255) NOT NULL,
            3Pper varchar(255) NOT NULL,
            FTper varchar(255) NOT NULL,
            OREB varchar(255) NOT NULL,
            DREB varchar(255) NOT NULL,
            REB varchar(255) NOT NULL,
            AST varchar(255) NOT NULL,
            STL varchar(255) NOT NULL,
            Turnover varchar(255) NOT NULL,
            PF varchar(255) NOT NULL,
            Team varchar(255) NOT NULL
            );

INSERT INTO Players20212022 (PlayerName,Number,Postions,GamesPlayed,Points,FG,FGper,3Pper,FTper,OREB,DREB,REB,AST,STL,Turnover,PF,Team) VALUES ('Marcus Smart ', '36 ', 'Guard ', '5   ', '76   ', '27   ', '39.7   ', '28.9   ', '78.6   ', '5   ', '12   ', '17   ', '34   ', '7   ', '13   ', '18   ', 'celtics');


INSERT INTO Players20212022 (PlayerName,Number,Postions,GamesPlayed,Points,FG,FGper,3Pper,FTper,OREB,DREB,REB,AST,STL,Turnover,PF,Team) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) 

grant all privileges on *.* to root@localhost identified by 'pass' with grant option;

CREATE USER root@localhost IDENTIFIED BY 'passpass';
grant all privileges on *.* to root@localhost with grant option;

ALTER USER 'root'@'localhost' IDENTIFIED BY 'Jutland1916!!';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Jutland1916!?';
FLUSH PRIVILEGES;

UPDATE mysql.user SET authentication_string=PASSWORD("Jutland1916!?")  WHERE user='root';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';