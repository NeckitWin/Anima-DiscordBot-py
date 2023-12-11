import disnake
from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | help.py ✅')

    @commands.slash_command(name="help", description="Помощь и мои команды")
    async def help(self, interaction):
        embed = disnake.Embed(title="Список моих команд:", color=interaction.author.color)
        embed.add_field(name="👑Административные:", value="</loggs:1180621713390714910> | </clear:1179587342655307776> | </prefix:1180255305230188554>", inline=False)
        embed.add_field(name="👤Пользовательские:",value="</user:1180637764803375115> | </banner:1180637764803375117> | </avatar:1180637764803375116> | </role:1180637764803375119>", inline=False)
        embed.add_field(name="✨Развлечения:",value="</ranime:1179418590529716224>", inline=False)
        embed.set_image(url="https://media.tenor.com/-Q_q8PALcRkAAAAC/hi-anime.gif")
        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))