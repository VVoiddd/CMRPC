import discord
from discord.ext import commands

class UserInfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        info = (
            f"User: {member.name}\n"
            f"Joined At: {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Roles: {', '.join([role.name for role in member.roles if role.name != '@everyone'])}"
        )
        await ctx.send(info)

def setup(bot):
    bot.add_cog(UserInfoCommand(bot))
