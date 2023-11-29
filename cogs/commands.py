import disnake
from disnake.ext import commands

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | commands.py ✅')

    @commands.command()
    async def servers(self, ctx):
        num = len(self.bot.guilds)
        await ctx.send(f"Количество серверов бота: {num}")

def setup(bot):
    bot.add_cog(Commands(bot))