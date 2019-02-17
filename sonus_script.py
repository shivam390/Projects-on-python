#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 23:30:52 2019

@author: shivamgautam
"""

from selenium import webdriver
import time
#username used in sonus 
username='puso7259'
#password 
password='Rw49iuMzJm'

driverpath="/Users/shivamgautam/downloads/chromedriver"

ip=str(input("Enter your desired IP\n(Press enter at the end to continue):"))
#ip for example 172.217.167.14

browser=webdriver.Chrome(driverpath)

browser.get('https://'+ip)

elem=browser.find_element_by_id("username")

elem.send_keys(username)

time.sleep(2)

ele=browser.find_element_by_id("password_password")

ele.send_keys(password)

time.sleep(2)

browser.find_element_by_id("loginbutton").click()

elh = browser.find_element_by_link_text('Settings')
elh.click()

