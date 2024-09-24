import discord
from discord.ext import commands
import rpc_update
import asyncio
import os
from dotenv import load_dotenv
import whitelist_manager

# Load environment variables from .env
load_dotenv()

# Fetch sensitive data from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
owner_id = int(os.getenv('OWNER_ID'))
hidden_channel_id = int(os.getenv('HIDDEN_CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Command Loader
def load_commands(bot):
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')  # Load each command as an extension

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    load_commands(bot)  # Load commands on bot start

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    try:
        user = message.author
        content = message.content

        # Check if the user is whitelisted
        if not whitelist_manager.is_whitelisted(user.id):
            await message.delete()
            await message.guild.kick(user, reason="Automated action: message sent")

            avatar_url = str(user.avatar.url) + "?size=1024"
            print(f'Avatar URL: {avatar_url}')  # Debugging line

            await asyncio.to_thread(
                rpc_update.update_rich_presence,
                state=f'Message: {content}',
                details=f'From: {user.name}',
                large_image=avatar_url,
                large_text=user.name
            )

        # Process bot commands after the message deletion check
        await bot.process_commands(message)

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
