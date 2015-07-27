#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import newspaper
import twitterpage
import time
import os
import configparser
import logging
logging.basicConfig(filename='/tmp/twitter-post.log',level=logging.DEBUG)

def getNewspaper(path):

    con = lite.connect('/home/nicolas/production/une2presse/une2presse.db')

    with con:    

        cur = con.cursor()
        cur.execute("SELECT * FROM Newspapers")

        rows = cur.fetchall()

        myNewspapers=[]

        for row in rows:
            myNewspapers.append(newspaper.Newspaper(row[0], row[1], row[2], row[3], path + row[4], row[5]))

        return myNewspapers;


# get application environment variable
appli_env = 'desktop'
if (os.getenv('APPLI_ENV')):
    appli_env = os.getenv('APPLI_ENV')

# Read configuration related to environment
config = configparser.ConfigParser();
config.read('une2presse.ini')
config_env = config[appli_env];
newspaper_path = config_env['newspaper_path']

twitter = twitterpage.MainPage()
twitter.signinTwitter()

Nps = getNewspaper(newspaper_path)

for myNewspaper in Nps:
    print "Download : "+myNewspaper.name
    logging.info("Download : "+myNewspaper.name)
    try:
        myNewspaper.downloadImage()
        if myNewspaper.compareMd5():
            twitter.tweetWithImage(myNewspaper.text, myNewspaper.folder + myNewspaper.filename, 1)
            time.sleep(20)
    except Error:
        logging.error("An error occur : "+Error)


