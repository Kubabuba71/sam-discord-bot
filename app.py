import asyncio
import json
import os

import apiai
import discord

client = discord.Client()
APIAI_CLIENT_ACCESS_TOKEN = '575980f2e29e40a5adc2dffca2843ef3'
ai = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)

def api_request(query):
    request = ai.text_request()
    request.session_id = 'discord'
    request.query = query
    response = request.getresponse()
    data = response.read()
    jsonData = json.loads(data)
    speech = jsonData["result"]["fulfillment"]["speech"]
    return speech

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!news'):
        response = api_request("What's in the news?")
        print(response)
        await client.send_message(message.channel, response)
    elif message.content.startswith('!sam'):
        query = message.content[5:]
        response = api_request(query)
        print(response)
        await client.send_message(message.channel, response)
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, 'wow test passed')
    elif message.content.startswith('!kappa'):
        await client.send_message(message.channel, 'http://i3.kym-cdn.com/photos/images/newsfeed/000/925/494/218.png_large')

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client.run(TOKEN)
