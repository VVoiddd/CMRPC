from discord.ext import commands
import whitelist_manager
import discord

class WhitelistCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="whitelist")
    async def whitelist(self, ctx, user: discord.User):
        whitelist_manager.add_to_whitelist(user.id)
        await ctx.send(f"{user.mention} has been added to the whitelist.")

    @commands.command(name="removefromwhitelist")
    async def removefromwhitelist(self, ctx, user: discord.User):
        whitelist_manager.remove_from_whitelist(user.id)
        await ctx.send(f"{user.mention} has been removed from the whitelist.")

    @commands.command(name="listwhitelist")
    async def listwhitelist(self, ctx):
        whitelisted_users = whitelist_manager.get_whitelist()
        if not whitelisted_users:
            await ctx.send("The whitelist is currently empty.")
        else:
            embed = discord.Embed(title="Whitelisted Users")
            for user_id in whitelisted_users:
                user = self.bot.get_user(user_id)
                if user:
                    embed.add_field(name=user.name, value=user.mention, inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(WhitelistCommands(bot))
