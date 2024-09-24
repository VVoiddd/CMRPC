from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(PingCommand(bot))