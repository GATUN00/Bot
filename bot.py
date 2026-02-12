import discord
from discord.ext import commands

# Create an instance of a Bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hello! How can I assist you?')

# Run the bot with your token
# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')
