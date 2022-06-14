# Made in collaboration again with the spectacular @sassycular bro


# Discord token for the bot is called packy because Stacky Packy is not Lacky ;)     - @sassycular

# xD

import discord
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random 

def RN(): return random.randint(0,10)

class questionObject:
  title = ""  # String Title
  body = ""  # Long String Body
  tags = []  # Linear array of tags
  # skipping tagged people attribute for now

def upload(question):
# Setting up options to run on repl
 chrome_options = Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')

# Not needed now. Implement later.
# To make selenium-chrome run in a headless state
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
 browser = webdriver.Chrome(options=chrome_options)

# Initialising Browser to team page
 browser.get("https://www.stackoverflow.com/c/UwU")
 time.sleep(RN())

# Accepting Cookies
 evilBtn = browser.find_element_by_class_name("js-accept-cookies")
 evilBtn.click()
 time.sleep(RN())

# Click on "I already have an account" option to login
 loginRadio = browser.find_element_by_id("has-public-account-radio")
 loginRadio.click()
 time.sleep(RN())

# Finding login elements
 email = browser.find_element_by_id("email")
 time.sleep(RN())
 pwd = browser.find_element_by_id("password")
 time.sleep(RN())
 submit = browser.find_element_by_id("submit-button")
 time.sleep(RN())

# Interacting with login elements
 email.send_keys("stacky@dndmeta.org")
 time.sleep(RN())
 pwd.send_keys(os.environ['password'])
 time.sleep(RN())
 submit.click()  # logs in successfully

# Navigating to new question page
 time.sleep(RN())  
#need to give prev page time to load else the next get command doesnt work
 browser.get("https://stackoverflow.com/c/uwu/questions/ask")

# Driver code for question object, to be imported from JSON later
 Q = question
  
 title = browser.find_element_by_id("title")
 time.sleep(RN())
 body = browser.find_element_by_class_name("js-editor")
 time.sleep(RN())
 tagsBar = browser.find_element_by_id("tageditor-replacing-tagnames--input")
 time.sleep(RN())
# (optional) ASK TEAM MEMBERS id: tageditor-replacing-mentionnames--input
 submit = browser.find_element_by_id("submit-button")

 time.sleep(RN())

 title.send_keys(Q.title)
 time.sleep(RN())
 body.send_keys(Q.body)

# Entering tags
 for tag in Q.tags:
  time.sleep(RN())
  tagsBar.send_keys(tag)
  time.sleep(RN())
  tagsBar.send_keys(" ")  # Spaces seperate tags on Stackoverflow

# finally submitting the question
 submit.click()
 time.sleep(RN())  # waiting for the confirmation box to load

# If a tag is new:
 try:
  tagConfirmation = browser.find_element_by_class_name(
    "js-confirm-tag-creation")
  tagConfirmation.click()
 except:
  pass
   # This should be enough to post a question
 time.sleep(10)
 print("FUNCTION COMPLETE UWU")

client = discord.Client()

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'): 
    await message.channel.send('Hello!')

  if message.content.startswith('$post'):
    text = message.content.split("$post ")[-1]
    #this is in an if do not indent or unindent
    # This is my Question #tag1 #tag2 #tag3
    Q = questionObject()
    quesTitle = text.split("#")[0]
    Q.tags = text.replace(" ","").split("#")
    Q.tags[0] = str(message.channel)
    Q.title = quesTitle
    Q.body = " "
    print(Q.title,"\n",Q.tags) # SaaS gaali deve (inside joke :P)
    # upload(Q)
    await message.reply('Your question has been posted! Sit back, your answer is on the way! :)')
    
  if message.content.startswith('$chai'):
    print(message.channel)

client.run(os.getenv('packy'))
