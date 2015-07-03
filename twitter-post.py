#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import newspaper
import twitterpage
import time

def getNewspaper():

    con = lite.connect('une2presse.db')

    with con:    

        cur = con.cursor()
        cur.execute("SELECT * FROM Newspapers")

        rows = cur.fetchall()

        myNewspapers=[]

        for row in rows:
            myNewspapers.append(newspaper.Newspaper(row[0], row[1], row[2], row[3], row[4], row[5]))

        return myNewspapers;


twitter = twitterpage.MainPage()
twitter.signinTwitter()

Nps = getNewspaper()

for myNewspaper in Nps:
    print "Download : "+myNewspaper.name
    myNewspaper.downloadImage()
    if myNewspaper.compareMd5():
        twitter.tweetWithImage(myNewspaper.text, myNewspaper.folder + myNewspaper.filename, 1)
        time.sleep(20)

