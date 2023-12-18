import discord
from googletrans import Translator

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual Discord bot token
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to monitor
TARGET_CHANNEL_ID = 'xxxxxxxxxxxxxxxxxxx'

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize the translator
translator = Translator()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Check if the message is from the target channel
    if str(message.channel.id) == TARGET_CHANNEL_ID:
        # Detect the language of the message
        source_language = translator.detect(message.content).lang

        # Check if the detected language is different from English
        if source_language != 'en':
                # Translate the message to English
                translation = translator.translate(message.content, dest='en')

                # Send the translated text to the same channel
                await message.channel.send(f'Translation ({source_language} to English): {translation.text}')

# Run the bot
client.run(TOKEN)