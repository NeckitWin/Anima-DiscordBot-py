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
        embed = disnake.Embed(title=f"Я постараюсь выполнить все твои мечты! А зовут меня {self.bot.user.name}", description=f"**{self.bot.user.mention}** - Я написанна для души, это моё имя", color=0x00ff00)
        embed.add_field(name="Как пользоваться?", value="Используй комманду /help", inline=False)
        embed.add_field(name="Количество серверов:", value=f"{len(self.bot.guilds)}", inline=True)
        embed.add_field(name="Количество пользователей:", value=f"{len(self.bot.users)}", inline=True)
        embed.add_field(name="Мой официальный дискорд сервер:", value="https://discord.gg/pA7hxfHy7A", inline=False)
        embed.add_field(name="Мой создатель NeckitWin", value="Связаться <@429562004399980546>", inline=False)
        embed.add_field(name="Мои разработчики:", value="NeckitWin и Enisey23", inline=False)
        embed.set_footer(text="Добавь меня на свой сервер няя <3")
        embed.set_author(name=f"Запрос от {interaction.author.name}")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/g75K3KA3VeAAAAAd/anime-sleep.gif")
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="user", description="Показывает информацию о пользователе")
    async def user(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, информацию которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        if member is None:
            member = interaction.author
        embed = disnake.Embed(title=f"Информация о пользователе {user.display_name}", description=f"Логин: **{user.name}**", color=member.color)
        embed.add_field(name="Роль", value=member.top_role.mention, inline=False)
        embed.add_field(name="Аккаунт создан", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="Присоединился на сервер", value=member.joined_at.strftime("%d.%m.%Y"), inline=True)
        if member.status == disnake.Status.online:
            embed.add_field(name="Статус", value="💚Онлайн💚", inline=False)
        elif member.status == disnake.Status.dnd:
            embed.add_field(name="Статус", value="❤️Не беспокоить❤️", inline=False)
        elif member.status == disnake.Status.idle:
            embed.add_field(name="Статус", value="💛Не активен💛", inline=False)
        elif member.status == disnake.Status.offline:
            embed.add_field(name="Статус", value="❔Оффлайн❔", inline=False)
        else:
            embed.add_field(name="Статус", value="Оч странно", inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)
        if user.banner is not None:
            embed.set_image(url=user.banner)
        embed.set_author(name=f"Запрос от {interaction.author.display_name}")
        embed.set_footer(text=f"Айди пользователя: {user.id}")
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

    #команда, которая выводит информацию о сервере, на сервере которому она была вызвана
    @commands.slash_command(name="server", description="Показывает информацию о сервере")
    async def server(self, interaction: disnake.CommandInteraction):
        embed = disnake.Embed(title=f"Информация о сервере {interaction.guild.name}", description=f"Владелец сервера: {interaction.guild.owner.mention}", color=0x2f3136)
        embed.add_field(name="Участники:", value=f"Всего:{len(interaction.guild.members)}", inline=True)
        embed.add_field(name="Количество текстовых каналов:", value=f"{len(interaction.guild.text_channels)}", inline=True)
        embed.add_field(name="Количество голосовых каналов:", value=f"{len(interaction.guild.voice_channels)}", inline=True)
        embed.add_field(name="Количество ролей:", value=f"{len(interaction.guild.roles)}", inline=True)
        embed.add_field(name="Количество категорий:", value=f"{len(interaction.guild.categories)}", inline=True)
        # покажи все роли сервера
        embed.set_thumbnail(url=interaction.guild.icon.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Infomod(bot))