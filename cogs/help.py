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
        embed = disnake.Embed(title="Список моих команд:", description="!help - покажет это окно\n\nУ всех моих команд есть описание, при вводе их в чате вы увидите их", color=interaction.author.color)
        embed.add_field(name="Команды для пользователей:", value="/avatar /banner /user /role - Информация и контент о участниках сервера", inline=False)
        embed.add_field(name="Помощь:",value="**/ranime** - Выбрать случайное аниме для просмотра", inline=False)
        embed.add_field(name="Показать эмоции:", value="/kiss /pat /hug /cry /bite /hit", inline=False)
        embed.add_field(name="Команды для администрации:", value="/prefix - Позволяет изменить префикс бота на своём сервере", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/-Q_q8PALcRkAAAAC/hi-anime.gif")
        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))