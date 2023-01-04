import discord
from dotenv import load_dotenv
import os

load_dotenv('token.env')
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hi!')

client.run(TOKEN)