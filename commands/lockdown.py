from discord.ext import commands
import discord
import asyncio

class LockdownCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx, duration: str):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Channel locked down.")
        
        time = self.convert_to_seconds(duration)
        await asyncio.sleep(time)

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("Channel unlocked.")

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
    bot.add_cog(LockdownCommand(bot))
