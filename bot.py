import discord
from dotenv import load_dotenv
import os
from webscraper import search_query
import tensorflow as tf

load_dotenv('token.env')
TOKEN = os.getenv('TOKEN')

model = tf.keras.models.load_model('model.h5')
vectorizing_model = tf.keras.models.load_model('vector_model.tf')
vectorizer = vectorizing_model.layers[0]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$search'):

        await message.channel.send('Searching...')

        results = search_query(message.content[7:])

        results = vectorizer(results)
        predictions = model.predict(results)
        overall = sum(predictions) / len(predictions)

        if overall > 0.5:
            await message.channel.send('The overall reviews are positive!')
        elif overall < 0.5:
            await message.channel.send('The overall reviews are negative!')

client.run(TOKEN)