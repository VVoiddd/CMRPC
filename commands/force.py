from discord.ext import commands
import rpc_update

class ForceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="force")
    async def force(self, ctx, *, message):
        avatar_url = str(ctx.author.avatar.url) + "?size=1024"

        # Force change the Rich Presence message and avatar
        rpc_update.update_rich_presence(
            state=f'Message: {message}',
            details=f'Forced by: {ctx.author.name}',
            large_image=avatar_url,
            large_text=ctx.author.name
        )
        await ctx.send(f'Rich Presence updated with message: "{message}".')

def setup(bot):
    bot.add_cog(ForceCommand(bot))
