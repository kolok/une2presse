#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(object):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def getTwitterPage(self):
        self.driver.get("http://twitter.com")

    def signinTwitter(self):
        self.getTwitterPage()
        signin = self.driver.find_element_by_id("signin-email")
        password = self.driver.find_element_by_id("signin-password")
        if signin:
            signin.send_keys("une2presse")
            password.send_keys("proute")
            password.send_keys(Keys.RETURN)

    def tweetWithImage(self, text, imageurl, click):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "tweet-box-home-timeline"))
            )
        finally:
            tweet = self.driver.find_element_by_id("tweet-box-home-timeline")
            tweet.send_keys(text)
            photo = self.driver.find_element_by_name("media_empty")
            photo.send_keys(imageurl)
            button = self.driver.find_element_by_class_name("tweet-action")
            if click:
                button.click()

    def close(self):
        self.driver.quit

