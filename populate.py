#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

# db description : une2presse
# sqlite3 une2presse
# create table newspapers (name varchar(50), frequency varchar(10), path varchar(255), folder varchar(255));
# -> frequency enum(daily, weekly, monthly)
# insert into newspapers ("Les Inrockultibles","weekly","http://www.revue2presse.fr/newspaper/lesinrocks/lesinrocks-cover.jpg","lesinrockultibles");
# insert into newspapers ("Liberation","weekly","http://www.revue2presse.fr/newspaper/liberation/liberation-cover.jpg","liberation");

# Top 10 of french newspapers
# 1	    LE MONDE	Paris
# 2	    LE FIGARO	Paris
# 3	    LE PARISIEN	Paris
# 4	    L´EQUIPE	Paris
# 5	    LIBERATION	Paris
# 6	    LE PROGRES	Lyon
# 7	    L´EXPRESS	Paris
# 8	    20 MINUTES	Paris
# 9	    LA TRIBUNE	Paris
# 10	LE POINT	Paris



newspapers = (
	("Le Monde","daily","http://www.revue2presse.fr/newspaper/lemonde/lemonde-cover.jpg", \
     "lemonde-cover.jpg","/Users/emilie/Documents/NewspaperCover/LeMonde/","Le Monde : http://www.lemonde.fr"),
	("Le Figaro","daily","http://www.revue2presse.fr/newspaper/lefigaro/lefigaro-cover.jpg", \
     "lefigaro-cover.jpg","/Users/emilie/Documents/NewspaperCover/LeFigaro/","Le Monde : http://www.lefigaro.fr"),
	("Le Parisien","daily","http://www.revue2presse.fr/newspaper/leparisien/leparisien-cover.jpg", \
     "leparisien-cover.jpg","/Users/emilie/Documents/NewspaperCover/LeParisien/","Le Parisien : http://www.leparisien.fr"),
	("L'Equipe","daily","http://www.revue2presse.fr/newspaper/lequipe/lequipe-cover.jpg", \
     "lequipe-cover.jpg","/Users/emilie/Documents/NewspaperCover/LEquipe/","L'Equipe : http://www.lequipe.fr"),
	("Liberation","daily","http://www.revue2presse.fr/newspaper/liberation/liberation-cover.jpg", \
     "liberation-cover.jpg","/Users/emilie/Documents/NewspaperCover/Liberation/","Liberation : http://www.liberation.fr")
)

con = lite.connect('une2presse.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Newspapers")
    cur.execute("CREATE TABLE Newspapers (Name varchar(50), Frequency varchar(10), Url varchar(255), \
                 FileName varchar(255), Folder varchar(255), Text varchar(255))")
    cur.executemany("INSERT INTO Newspapers VALUES(?, ?, ?, ?, ?, ?)", newspapers)
