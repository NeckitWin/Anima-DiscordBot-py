import disnake
from disnake.ext import commands

class Infomod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | infomod.py ✅')

    @commands.slash_command(name="bot", description="Основная информация о Anima")
    async def bot(self,interaction):
        embed = disnake.Embed(title=f"Я выполнила твою команду! Меня зовут {self.bot.user.name}", description=f"**{self.bot.user.mention}** Я написанна для души", color=0x00ff00)
        embed.add_field(name="Как пользоваться?", value="Используйте комманду /help", inline=False)
        embed.add_field(name="Количество серверов:", value=f"{len(self.bot.guilds)}", inline=True)
        # с помощью for посчитай всех пользователей на всех серверах и выведи число
        embed.add_field(name="Количество пользователей:", value=f"{len(self.bot.users)}", inline=True)
        embed.add_field(name="Мой официальный дискорд сервер:", value="https://discord.gg/pA7hxfHy7A", inline=False)
        embed.set_footer(text="Добавь меня на свой сервер няя <3")
        embed.set_author(name=f"Запрос от {interaction.author.name}")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/g75K3KA3VeAAAAAd/anime-sleep.gif")
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="user", description="Показывает информацию о пользователе")
    async def user(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, информацию которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        embed = disnake.Embed(title="Информация о пользователе", description=f"Имя: {user.name}\nID: {user.id}", color=0x2f3136)
        embed.set_thumbnail(url=user.display_avatar.url)
        if user.banner is not None:
            embed.set_image(url=user.banner)
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="avatar", description="Показывает аватар пользователя")
    async def avatar(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, аватар которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        if user.display_avatar.url is None:
            await interaction.response.send_message("У этого пользователя нет аватара!", ephemeral=True)
        else:
            embed = disnake.Embed(title="Вы запросили аватар", description=f"Пользователя {user.mention}", color=0xa269ff)
            embed.set_image(url=user.display_avatar.url)
            await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="banner", description="Показывает баннер пользователя")
    async def banner(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, баннер которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        if user.banner is None:
            await interaction.response.send_message("У этого пользователя нет баннера!", ephemeral=True)
        else:
            embed = disnake.Embed(title="Вы запросили баннер", description=f"Пользователя {user.mention}", color=0xa269ff)
            embed.set_image(url=user.banner)
            await interaction.response.send_message(embed=embed)
# ephemeral=True покажет фантомное предложение
def setup(bot):
    bot.add_cog(Infomod(bot))