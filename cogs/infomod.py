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
        embed = disnake.Embed(title=f"Я постараюсь выполнить все твои мечты! А зовут меня {self.bot.user.name}", color=0x00ff00)
        embed.add_field(name="Как мною пользоваться?", value="Используй комманду /help", inline=False)
        embed.add_field(name="Количество пользователей:", value=f"{len(self.bot.users)}", inline=True)
        embed.add_field(name="Количество серверов:", value=f"{len(self.bot.guilds)}", inline=True)
        embed.add_field(name="Мой основатель:", value="NeckitWin <@429562004399980546>", inline=False)
        embed.add_field(name="Мои разработчики:", value="NeckitWin Enisey23", inline=True)
        embed.add_field(name="Мой официальный дискорд сервер:", value="[Перейти на сервер](https://discord.gg/pA7hxfHy7A)", inline=True)
        embed.set_footer(text="Добавь меня на свой сервер няя <3")
        embed.set_author(name=f"Запрос от {interaction.author.name}", icon_url=interaction.author.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/g75K3KA3VeAAAAAd/anime-sleep.gif")
        await interaction.response.send_message(embed=embed)



    @commands.slash_command(name="user", description="Показывает информацию о пользователе")
    async def user(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, информацию которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        if member is None:
            member = interaction.author
        embed = disnake.Embed(title=f"Информация о пользователе {user.display_name}", description=f"Логин: **{user.name}** | {user.mention}", color=member.color)
        embed.add_field(name="Высшая роль", value=member.top_role.mention, inline=False)
        embed.add_field(name="Аккаунт создан", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="Присоединился на сервер", value=member.joined_at.strftime("%d.%m.%Y"), inline=True)
        if member.status == disnake.Status.online:
            embed.add_field(name="Статус", value="<:busy:1183433301231415388> | Онлайн", inline=False)
        elif member.status == disnake.Status.dnd:
            embed.add_field(name="Статус", value="<:busy:1183433301231415388> | Не беспокоить", inline=False)
        elif member.status == disnake.Status.idle:
            embed.add_field(name="Статус", value="<:idle:1183433294596034651> | Не активен", inline=False)
        elif member.status == disnake.Status.offline:
            embed.add_field(name="Статус", value="<:offline:1183433298878410772> | Оффлайн", inline=False)
        else:
            embed.add_field(name="Статус", value="❔ | Очень странно", inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)
        if user.banner is not None:
            embed.set_image(url=user.banner)
        embed.set_author(name=f"Запрос от {interaction.author.display_name}", icon_url=interaction.author.avatar.url)
        embed.set_footer(text=f"Айди пользователя: {user.id}")
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="avatar", description="Показывает аватар пользователя")
    async def avatar(self, interaction: disnake.CommandInteraction,
                     member: disnake.Member = commands.Param(lambda i: i.author, name="member",
                                                             description="Пользователь, аватар которого нужно посмотреть")):
        embed1 = disnake.Embed(title="Вы запросили аватар", description=f"Пользователя {member.mention}",
                               color=interaction.author.color)
        if member.avatar.url is not None:
            embed1.set_image(url=member.avatar.with_size(512).url)
        else:
            embed1.add_field(name="Обычный Аватар", value="У этого пользователя нет обычного аватара.")
        embed2 = disnake.Embed(title="Серверный аватар", description=f"Пользователя {member.mention}",
                               color=0xa269ff)
        if member.display_avatar.url is not None:
            embed2.set_image(url=member.display_avatar.with_size(512).url)
        else:
            embed2.add_field(name="Дисплей-Аватар", value="У этого пользователя нет дисплей-аватара.")

        # Отправляем оба эмбеда в одном сообщении
        await interaction.response.send_message(embeds=[embed1, embed2])

    @commands.slash_command(name="banner", description="Показывает баннер пользователя")
    async def banner(self, interaction: disnake.CommandInteraction, member: disnake.Member = commands.Param(lambda i: i.author, name="member", description="Пользователь, баннер которого нужно посмотреть")):
        user = await self.bot.fetch_user(member.id)
        if user.banner is None:
            await interaction.response.send_message("У этого пользователя нет баннера!", ephemeral=True)
        else:
            embed = disnake.Embed(title="Вы запросили баннер", description=f"Пользователя {user.mention}", color=0xa269ff)
            embed.set_image(url=user.banner)
            await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="server", description="Показывает информацию о сервере")
    async def server(self, interaction: disnake.CommandInteraction):
        embed = disnake.Embed(title=f"Информация о сервере {interaction.guild.name}", description=f"Владелец сервера: {interaction.guild.owner.mention}", color=0x2f3136)
        embed.add_field(name="Участники:", value=f"Всего:{len(interaction.guild.members)}", inline=True)
        embed.add_field(name="Количество текстовых каналов:", value=f"{len(interaction.guild.text_channels)}", inline=True)
        embed.add_field(name="Количество голосовых каналов:", value=f"{len(interaction.guild.voice_channels)}", inline=True)
        embed.add_field(name="Количество ролей:", value=f"{len(interaction.guild.roles)}", inline=True)
        embed.add_field(name="Количество категорий:", value=f"{len(interaction.guild.categories)}", inline=True)
        embed.set_thumbnail(url=interaction.guild.icon.url)
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="role", description="Показывает информацию о роли")
    async def role(self, interaction: disnake.CommandInteraction, role: disnake.Role):
        embed = disnake.Embed(title=f"Информация о роли {role.name}", description=f"Внешность роли: {role.mention} \n", color=0x2f3136)
        embed.add_field(name=f"Количество владельцев роли:", value=f"{len(role.members)}", inline=True)
        embed.add_field(name="Уровень роли:", value=f"{role.position}", inline=True)
        embed.add_field(name="Цвет роли:", value=f"{role.color}", inline=True)
        embed.add_field(name="ID роли:", value=f"```{role.id}```", inline=True)
        embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Infomod(bot))