# This code also depicts how to run selenium bots on an online ide like repl
# Personal note: @sassycular never shows up on time. Average time wasted daily on waiting: ~1.5hrs (based on a data of 4 days)
# Is wasting 90 mintues a day worth it ?

# Coded by Krypto-Kiddo for StrawHats DAO

# Importing Stuff ... bruh
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time  # i can control time :3

# Setting up options to run on repl
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Not needed now. Implement later.
'''# To make selenium-chrome run in a headless state
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')'''

browser = webdriver.Chrome(options=chrome_options)


# Defining question structure as a class
class question:
    title = ""  # String Title
    body = ""  # Long String Body
    tags = []  # Linear array of tags
    # skipping tagged people attribute for now


# Initialising Browser to team page
browser.get("https://www.stackoverflow.com/c/UwU")
time.sleep(5)

# Accepting Cookies
evilBtn = browser.find_element_by_class_name("js-accept-cookies")
evilBtn.click()

# Click on "I already have an account" option to login
loginRadio = browser.find_element_by_id("has-public-account-radio")
loginRadio.click()

# Finding login elements
email = browser.find_element_by_id("email")
pwd = browser.find_element_by_id("password")
submit = browser.find_element_by_id("submit-button")

# Interacting with login elements
email.send_keys("stackbot@dndmeta.org")
pwd.send_keys(os.environ['password'])
submit.click()  # logs in successfully

# Navigating to new question page
time.sleep(
    5
)  # need to give prev page time to load else the next get command doesnt work
browser.get("https://stackoverflow.com/c/uwu/questions/ask")

# Driver code for question object, to be imported from JSON later
Q = question()
Q.title = "Can we run selenium bots online ?"
Q.body = "If we can possibly run selenium bots online then we could make a discord bot to post questions and answers to stackoverflow teams! Yaay"
Q.tags = ["Selenium", "Bots", "Stackoverflow", "StackBot"]

title = browser.find_element_by_id("title")
body = browser.find_element_by_class_name("js-editor")
tagsBar = browser.find_element_by_id("tageditor-replacing-tagnames--input")
# (optional) ASK TEAM MEMBERS id: tageditor-replacing-mentionnames--input
submit = browser.find_element_by_id("submit-button")

title.send_keys(Q.title)
body.send_keys(Q.body)

# Entering tags
for tag in Q.tags:
    tagsBar.send_keys(tag)
    tagsBar.send_keys(" ")  # Spaces seperate tags on Stackoverflow

# finally submitting the question
submit.click()
time.sleep(1)  # waiting for the confirmation box to load

# If a tag is new:
try:
    tagConfirmation = browser.find_element_by_class_name(
        "js-confirm-tag-creation")
    tagConfirmation.click()
except:
    pass

# This should be enough to post a question
