import discord
from discord.ext import commands

class UnmuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention} has been unmuted.")

def setup(bot):
    bot.add_cog(UnmuteCommand(bot))
