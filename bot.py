import discord
from discord.ext import commands
import json
import os
from rpc_update import update_rich_presence
import asyncio

# Configuration
INVITE_URL = "https://discord.gg/YOUR_INVITE_LINK"  # Set your invite link here
HIDDEN_CHANNEL_ID = 0  # Channel where RPC should be updated and other actions should happen
COMMAND_CHANNELS = 0  # Can be a single channel ID or a list of channel IDs
OWNER_ID = 0  # Replace with your Discord user ID
WHITELIST_FILE = 'whitelist.json'
CLIENT_ID = 'YOUR_CLIENT_ID'  # Your application Client ID

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

# Initialize Discord Rich Presence with CLIENT_ID from bot.py
rpc = update_rich_presence(CLIENT_ID)

# Load whitelist from JSON
def load_whitelist():
    """Loads the whitelist from the JSON file, creates it if not exists."""
    if not os.path.exists(WHITELIST_FILE):
        with open(WHITELIST_FILE, 'w') as f:
            json.dump({}, f, indent=4)
    with open(WHITELIST_FILE, 'r') as f:
        return json.load(f)

# Save whitelist to JSON
def save_whitelist(whitelist_data):
    """Saves the whitelist data to the JSON file."""
    with open(WHITELIST_FILE, 'w') as f:
        json.dump(whitelist_data, f, indent=4)

# Update Rich Presence (asynchronous wrapper)
async def update_rich_presence_on_message(state, details, large_image, large_text):
    """Updates the Discord Rich Presence with provided details asynchronously."""
    try:
        # Update Rich Presence in a separate thread to avoid blocking
        await asyncio.to_thread(rpc.update,  
            state=state,
            details=details,
            large_image=large_image,
            large_text=large_text,
            buttons=[{"label": "Join Discord", "url": INVITE_URL}]  # Use the global invite URL here
        )
        print(f"Rich Presence updated: {state} | {details} | Hover Text: {large_text}")
    except Exception as e:
        print(f"Error updating Rich Presence: {e}")

# Load the whitelist on bot startup
whitelist_data = load_whitelist()

@bot.event
async def on_ready():
    """Sets the default Rich Presence when the bot starts."""
    print(f"Logged in as {bot.user}")
    await update_rich_presence_on_message("Type what you want and it will be here", "Your username would be here", "placeholder", "This can be your PFP")
    print("Default Rich Presence initialized.")

@bot.event
async def on_message(message):
    """Handles messages and updates Rich Presence dynamically."""
    global COMMAND_CHANNELS  # Ensure the global COMMAND_CHANNELS variable is accessible here

    if message.author == bot.user:
        return

    # Ensure the whitelist is loaded correctly
    whitelist_data = load_whitelist()

    # Convert user ID to string for comparison
    user_id_str = str(message.author.id)

    # Ensure COMMAND_CHANNELS is iterable (can be either a single channel ID or a list)
    if isinstance(COMMAND_CHANNELS, int):
        COMMAND_CHANNELS = [COMMAND_CHANNELS]  # Ensure it's a list if it's a single ID

    # Only process messages in the command channels
    if message.channel.id in COMMAND_CHANNELS:
        # Handle commands but do not update the RPC here
        await bot.process_commands(message)

    # For the HIDDEN_CHANNEL_ID, perform actions and update Rich Presence
    elif message.channel.id == HIDDEN_CHANNEL_ID:
        # Check if the user is not whitelisted and is not the owner
        if user_id_str not in whitelist_data and message.author.id != OWNER_ID:
            # Non-whitelisted user: Delete message, update RPC, and kick the user
            await message.delete()  # Delete message
            await message.channel.send(f"{message.author.mention}, you are not whitelisted!")  # Notify user

            # Fetch the user's avatar URL before kicking
            avatar_url = message.author.display_avatar.url if message.author.display_avatar else "placeholder"
            
            # Update Rich Presence with the avatar URL before kicking
            await update_rich_presence_on_message(f"Message: {message.content}", f"From: {message.author.name}", avatar_url, message.author.name)
            
            await message.guild.kick(message.author, reason="Non-whitelisted user")  # Kick the user
            # Send a DM with a new invite
            try:
                await message.author.send(f"You've been kicked for not being whitelisted. Here is a new invite: {INVITE_URL}")
            except discord.Forbidden:
                print(f"Could not send DM to {message.author.name}")
            return  # Prevent further processing for non-whitelisted users

        # If the user is whitelisted or the owner, just delete the message and update RPC
        if user_id_str in whitelist_data or message.author.id == OWNER_ID:
            await message.delete()  # Delete message for whitelisted users
            avatar_url = message.author.display_avatar.url if message.author.display_avatar else "placeholder"
            await update_rich_presence_on_message(message.content or "Type what you want and it will be here", f"From: {message.author.name}", avatar_url, message.author.name)
            print(f"Rich Presence updated for {message.author.name}: {message.content}")

@bot.command()
async def whitelist(ctx, user: discord.User):
    """Adds a user to the whitelist."""
    whitelist_data = load_whitelist()

    if user.id not in whitelist_data:
        # Add to whitelist and save
        whitelist_data[user.id] = {
            'username': user.name,
            'uid': user.id
        }
        save_whitelist(whitelist_data)

        # Send success embed
        embed = discord.Embed(
            title="Whitelist Update",
            description=f"{user.mention} has been added to the whitelist.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{user.mention} is already whitelisted.")

@bot.command()
async def listwhitelist(ctx):
    """Lists all whitelisted users."""
    whitelist_data = load_whitelist()  # Load whitelist on each command call
    if not whitelist_data:
        await ctx.send("No users are currently whitelisted.")
    else:
        whitelisted_users = [f"{data['username']} (ID: {user_id})" for user_id, data in whitelist_data.items()]
        embed = discord.Embed(
            title="Whitelisted Users",
            description="\n".join(whitelisted_users) if whitelisted_users else "No users found.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

@bot.command()
async def removewhitelist(ctx, user: discord.User):
    """Removes a user from the whitelist."""
    whitelist_data = load_whitelist()

    if user.id in whitelist_data:
        del whitelist_data[user.id]
        save_whitelist(whitelist_data)

        # Send success embed
        embed = discord.Embed(
            title="Whitelist Update",
            description=f"{user.mention} has been removed from the whitelist.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{user.mention} is not in the whitelist.")

@bot.command()
async def force(ctx, *, message: str):
    """Forces a custom Rich Presence update."""
    if ctx.author.id == OWNER_ID:
        await update_rich_presence_on_message(message, "Custom Rich Presence", "placeholder", "This can be your PFP")
        await ctx.send(f"Rich Presence updated to: {message}")
    else:
        await ctx.send("You do not have permission to use this command.")

if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN')  # Replace with your bot's token
