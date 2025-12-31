
import discord
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = response.json()
    return json_data['url']

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content.startswith('$chambea'):
            await message.channel.send('callate miguel')

client = MyClient(intents=intents)
client.run(TOKEN)
