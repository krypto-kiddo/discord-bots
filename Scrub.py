# SCRUB : Summarization of Content Under a Bot 
# UwU

# Scrub is a discord bot that retrieves channel message history, summarizes it using an integrated ML model and tells you in short what happened on the server while you were away

from transformers import pipeline
model = pipeline("summarization")

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('Scrub what do you rub?'):
        await message.channel.send('Oh my god, are you for real ?!')
    elif message.content.startswith('$sum'): # Returns all texts in the channel, as a message, with a # seperator.
        listMsg = ""
        async for msg in message.channel.history(): # you can change limit as ...history(limit=10000)
            # using without an async will give an iterability error. . . weird
            listMsg+=(str(msg.content)+"#")
        await message.channel.send(listMsg)
    elif message.content.startswith('$txtsum'):
        sumtxt = open("history.txt","w")
        async for msg in message.channel.history():
            if msg.author != client.user:
                try: sumtxt.write(str(msg.content))
                except: pass
        sumtxt.close()
        print("file saved")
        sumtxt = open("history.txt","r")
        await message.channel.send(file=discord.File(sumtxt,'Message History.txt'))
        sumtxt.close()
    elif message.content.startswith('$whathappened'):
      text = ""
      async for msg in message.channel.history():
        if msg.author!=client.user:
          try: text+=(str(msg.content)+" ")
          except: pass
      summary = model(text)
      print("\n\nTHIS IS THE SUMMARY TEXT FED INTO THE MODEL : ",text,"\n\n")
      await message.channel.send(summary)






client.run('YOUR TOKEN HERE!')
