import disnake
from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | help.py ✅')

    @commands.command()
    async def help(self,ctx):
        embed = disnake.Embed(title="Список моих команд:", description="!help - покажет это окно", color=0x00ff00)
        embed.add_field(name="Команды для пользователей:", value="", inline=False)
        embed.add_field(name="/avatar /banner /user", value="Информация и контент о участниках сервера", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/-Q_q8PALcRkAAAAC/hi-anime.gif")
        await ctx.send(embed=embed)

    @commands.slash_command(name="help", description="Помощь и мои команды")
    async def help(self, interaction):
        embed = disnake.Embed(title="Список моих команд:", description="!help - покажет это окно", color=0x00ff00)
        embed.add_field(name="Команды для пользователей:", value="", inline=False)
        embed.add_field(name="/avatar /banner /user", value="Информация и контент о участниках сервера", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/-Q_q8PALcRkAAAAC/hi-anime.gif")
        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))