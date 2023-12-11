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

    @commands.slash_command(name="баланс", description="Показывает ваш баланс")
    async def balance(self, inter, member: disnake.Member = None):
        if not member:
            member = inter.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(title=f"Баланс {member}", color=0x2f3136)
        embed.add_field(name="🪙Деньги", value=f"```{user[1]}```")
        embed.add_field(name="💎Гемы", value=f"```{user[2]}```")
        embed.set_thumbnail(url=member.avatar.url)
        await inter.response.send_message(embed=embed)



def setup(bot):
    bot.add_cog(Levels(bot))