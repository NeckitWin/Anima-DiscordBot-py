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

    @commands.command(name="help", description="Помощь и мои команды")
    async def help(self,ctx):
        embed = disnake.Embed(title="Список моих команд:", description="!help - покажет это окно", color=ctx.author.color)
        embed.add_field(name="Команды для пользователей:", value="/avatar /banner /user - Информация и контент о участниках сервера\n"
                                                                 "/ranime - Выбрать случайное аниме для просмотра", inline=False)

        embed.add_field(name="Команды для администрации:", value="/prefix - Позволяет изменить префикс бота на своём сервере", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))