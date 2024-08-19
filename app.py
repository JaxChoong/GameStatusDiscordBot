import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
# Set up the bot with the appropriate intents
intents = discord.Intents.default()
intents.presences = True  # Enable presence intent
intents.members = True  # Enable members intent
bot = commands.Bot(command_prefix="!", intents=intents)

# Your bot's token
TOKEN = os.getenv("BOT_TOKEN")

# The game you want to track                                                                                
TARGET_GAME = "Overwatch 2"

# Event to detect presence updates
@bot.event
async def on_presence_update(before, after):
    # Check if the user has started playing the target game
    if after.activity and after.activity.name == TARGET_GAME:
        # Send a message in a specific channel
        channel = discord.utils.get(after.guild.channels, name="general")
        if channel:
            await channel.send(f"{after.name} is now playing {TARGET_GAME}!")

# Run the bot
bot.run(TOKEN)
