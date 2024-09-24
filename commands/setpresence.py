import discord
from discord.ext import commands

class SetPresenceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setpresence(self, ctx, state: str, *, details: str):
        await self.bot.change_presence(activity=discord.Game(name=state), status=discord.Status.online)
        await ctx.send(f"Presence set to: {state} - {details}")

def setup(bot):
    bot.add_cog(SetPresenceCommand(bot))
