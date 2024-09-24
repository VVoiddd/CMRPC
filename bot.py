import discord
from discord.ext import commands
import rpc_update
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
hidden_channel_id = REPLACE-WITH-CHANNEL-ID
owner_id = REPLACE-WITH-OWNER-ID

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

        await message.delete()

        if user.id != owner_id:
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

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    bot.run('TOKEN')
