# A discord bot that queries questions from stackoverflow and gives back top 5 answers matching your query.
# Built in collaboration with @sassycular
# Programmed for Strawhats DAO by @krypto-kiddo

import discord
import os
import requests
import json

client = discord.Client()

@client.event 
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(msg):

  # test command
  if msg.content.startswith("$hello"):
    await msg.channel.send("Hello human world! I am alive!!")
    
  elif msg.content.startswith("$ask"): # ask command 
    
    # Retrieving question string from message
    query = msg.content.split("$ask ")[-1] 
    
    # replacing spaces with + for api query
    query = query.replace(" ","+") 

    # building final query string
    query = "https://api.stackexchange.com/search/advanced?site=stackoverflow.com&q=" + query

    # GET query
    res = requests.get(query)

    # parse query result text as JSON
    obj = json.loads(res.text)

    # giving back top 5 questions matching search results
    for i in range(5):
      try: await msg.channel.send(obj["items"][i]["link"])
      except: pass # excpetion for if index out of range
    
    # Reporting back how much search quota is left.
    await msg.channel.send("Queries remaining for current session : "+str(obj["quota_remaining"]))
      
# intialising the client    
client.run(os.environ.get('TOKEN'))
