from discord.ext import commands

class PurgeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)  # +1 to delete the command message
        await ctx.send(f"Deleted {amount} messages.", delete_after=5)

def setup(bot):
    bot.add_cog(PurgeCommand(bot))
