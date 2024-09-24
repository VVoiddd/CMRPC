from discord.ext import commands

class BroadcastCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def broadcast(self, ctx, *, message: str):
        for channel in ctx.guild.text_channels:
            await channel.send(message)
        await ctx.send("Broadcast sent to all channels.")

def setup(bot):
    bot.add_cog(BroadcastCommand(bot))
