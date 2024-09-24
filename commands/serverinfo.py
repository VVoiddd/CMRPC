from discord.ext import commands

class ServerInfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        info = (
            f"Server Name: {guild.name}\n"
            f"Total Members: {guild.member_count}\n"
            f"Region: {guild.region}\n"
            f"Created At: {guild.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        await ctx.send(info)

def setup(bot):
    bot.add_cog(ServerInfoCommand(bot))
