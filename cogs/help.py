import disnake
from disnake.ext import commands


async def help(interaction, title, text):
    embed = disnake.Embed(title=title, color=interaction.author.color)
    embed.add_field(name=f"👑{text[0]}",
                    value="</loggs:1180621713390714910> `|` </clear:1179587342655307776> `|` </prefix:1180255305230188554>",
                    inline=False)
    embed.add_field(name=f"🛡{text[1]}:", value="</clear:1179587342655307776>", inline=False)
    embed.add_field(name=f"👤{text[2]}:",
                    value="</user:1180637764803375115> | </banner:1180637764803375117> | </avatar:1180637764803375116> | </role:1180637764803375119>",
                    inline=False)
    embed.add_field(name=f"🏆{text[3]}:", value="</top:1184263611108053134> | </level:1184258420019310614>",
                    inline=False)
    embed.add_field(name=f"🔧{text[4]}:", value="</ranime:1179418590529716224>", inline=False)
    embed.add_field(name=f"✨{text[5]}:",
                    value="</bite:1180274346913173537> | </cry:1180274346913173536> | </hug:1180274346913173535> | </kiss:1180269189458579477> | </pat:1180274346913173534> | </hit:1180282596853293167>",
                    inline=False)
    embed.set_image(url="https://media.tenor.com/-Q_q8PALcRkAAAAC/hi-anime.gif")
    await interaction.send(embed=embed)

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | help.py ✅')
    @commands.slash_command(name="help", description="Помощь и мои команды")
    async def help(self, interaction):
        await help(interaction, title="Список моих команд, няя <3", text=["Административные", "Модерация", "Пользовательские", "Достижения", "Утилиты", "Развлечения"])


def setup(bot):
    bot.add_cog(Help(bot))