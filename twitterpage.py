#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class MainPage(object):

    def __init__(self):
#        chromedriver = "/Users/emilie/Documents/workspace/une2presse/chromedriver"
#        os.environ["webdriver.chrome.driver"] = chromedriver
        display = Display(visible=0, size=(800, 800))
        display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            "/usr/local/bin/chromedriver",
            chrome_options=chrome_options
        )

    def getTwitterPage(self):
        self.driver.get("http://twitter.com")

    def signinTwitter(self):
        self.getTwitterPage()
        signin = self.driver.find_element_by_id("signin-email")
        password = self.driver.find_element_by_id("signin-password")
        if signin:
            signin.send_keys("une2presse")
            time.sleep(3)
            password.send_keys("proute")
            password.send_keys(Keys.RETURN)

    def tweetWithImage(self, text, imageurl, click):
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "tweet-box-home-timeline"))
            )
        finally:
            tweet = self.driver.find_element_by_id("tweet-box-home-timeline")
            tweet.send_keys(text)
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "media_empty"))
            )
        finally:
            photo = self.driver.find_element_by_name("media_empty")
            photo.send_keys(imageurl)
        button = self.driver.find_element_by_class_name("tweet-action")
        if click:
            button.click()

    def close(self):
        self.driver.quit

