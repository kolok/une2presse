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
import time

logging.basicConfig(filename='/tmp/twitter-post.log',level=logging.INFO)

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


logging.info("Job is launched at " + time.strftime("%d/%m/%Y %H:%M:%S"))

logging.info("Read config file")

# get application environment variable
appli_env = 'desktop'
if (os.getenv('APPLI_ENV')):
    appli_env = os.getenv('APPLI_ENV')

# Read configuration related to environment
config = configparser.ConfigParser();
config.read('/home/nicolas/production/une2presse/une2presse.ini')
config_env = config[appli_env];
newspaper_path = config_env['newspaper_path']

logging.info("Sign in to twitter")

twitter = twitterpage.MainPage()
twitter.signinTwitter()

logging.info("Get action from DB")

Nps = getNewspaper(newspaper_path)

for myNewspaper in Nps:
    logging.info("Download " + myNewspaper.name)
    try:
        myNewspaper.downloadImage()
        if myNewspaper.compareMd5():
            logging.info("Tweet " + myNewspaper.name)
            twitter.tweetWithImage(myNewspaper.text, myNewspaper.folder + myNewspaper.filename, 1)
            time.sleep(20)
    except ValueError:
        logging.error("An error occur : "+Error)

logging.info("close the browser")
twitter.close()

