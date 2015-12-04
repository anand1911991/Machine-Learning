__author__ = 'lenovo-pc'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

driver = webdriver.Firefox()
driver.get("https://www.irctc.co.in")
driver.find_element_by_id("usernameId").clear()
driver.find_element_by_id("usernameId").send_keys("seraph19")
driver.find_element_by_name("j_password").clear()
driver.find_element_by_name("j_password").send_keys("argetlam")
time.sleep(7)
driver.find_element_by_id("loginbutton").click()
driver.get(driver.current_url)
driver.find_element_by_id("jpform:fromStation").clear()
driver.find_element_by_id("jpform:fromStation").send_keys("NDLS")
driver.find_element_by_id("jpform:toStation").clear()
driver.find_element_by_id("jpform:toStation").send_keys("LKO")
driver.find_element_by_id("jpform:journeyDateInputDate").clear()
driver.find_element_by_id("jpform:journeyDateInputDate").send_keys("25-11-2015")
driver.find_element_by_id("jpform:jpsubmit").click()




