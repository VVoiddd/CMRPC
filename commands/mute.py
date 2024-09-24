import discord
from discord.ext import commands
import asyncio

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, duration: str):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")  # Ensure you have a 'Muted' role
        await member.add_roles(mute_role)
        await ctx.send(f"{member.mention} has been muted for {duration}.")
        
        # Convert duration to seconds
        time = self.convert_to_seconds(duration)
        await asyncio.sleep(time)
        
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention} has been unmuted.")

    def convert_to_seconds(self, duration):
        unit = duration[-1]
        amount = int(duration[:-1])
        if unit == 's':
            return amount
        elif unit == 'm':
            return amount * 60
        elif unit == 'h':
            return amount * 3600
        elif unit == 'd':
            return amount * 86400
        return amount  # Default to seconds if invalid

def setup(bot):
    bot.add_cog(MuteCommand(bot))
