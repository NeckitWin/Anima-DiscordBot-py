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
        servers_list = []
        for guild in self.bot.guilds:
            servers_list.append(guild.name)
        servers_list = ", ".join(servers_list)
        await ctx.send(f"Сервера бота: {servers_list}")

def setup(bot):
    bot.add_cog(Commands(bot))