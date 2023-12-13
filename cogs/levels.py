import disnake
from disnake.ext import commands
from utils.databases import UserDB

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UserDB()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | levels.py ✅')

    @commands.command(name="createdb")
    async def createdb(self, ctx):
        if ctx.author.id == 429562004399980546:
            await self.db.create_table()
            await ctx.send("Таблица создана")
        else:
            await ctx.send("У вас нет прав")

    @commands.slash_command(name="level", aliases=["lvl"], description="Показывает ваш уровень либо уровень упомянутого пользователя")
    async def level(self, ctx, member: disnake.Member = None):
        if not member:
            member = ctx.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(title=f"Уровень {member}", color=0x2f3136)
        embed.add_field(name="✨Количество опыта:", value=f"```{user[2]}```")
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.slash_command(name="top", description="Показывает самых общительных пользователей")
    async def top(self, ctx):
        top = await self.db.get_top()
        embed = disnake.Embed(title="Мировая таблица опыта!", description="**Просто общайся**, и получай опыт, няя <3", color=0x00ff00)
        for i in range(len(top)):
            if i == 0:
                embed.add_field(name=f"🥇 {top[i][1]}", value=f"`Первое место {top[i][2]} опыта`", inline=False)
            elif i == 1:
                embed.add_field(name=f"🥈 {top[i][1]}", value=f"`Второе место {top[i][2]} опыта`", inline=False)
            elif i == 2:
                embed.add_field(name=f"🥉 {top[i][1]}", value=f"`Третье место {top[i][2]} опыта`", inline=False)
            else:
                embed.add_field(name=f"#{i + 1} {top[i][1]}", value=f"`{top[i][2]} опыта`", inline=False)
        embed.set_image(url="https://i.pinimg.com/originals/67/c4/3e/67c43e28053fa2cb1ca5d7e267cd1907.gif")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.db.add_user(message.author)
        await self.db.update_user(message.author)

def setup(bot):
    bot.add_cog(Levels(bot))