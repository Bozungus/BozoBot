import discord
import os
import base64

clientKey = base64.b64decode("T1RrMU5UQTJNVEl3TWpFM01EZ3pPVEkwLkdtd09yUS5uRmNUOVgyREhCMnVsQXg3LWpYX2xJTjhXS3VWNVI0MTN4QXRLWQ==").decode("utf-8", "ignore")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('!help: shows possible commands, !stop: shuts down all bot function (user specific)')

    if message.content.startswith("!stop"):
        if message.author.id == 644355525277908992:
            await exit()     


 
client.run(clientKey)