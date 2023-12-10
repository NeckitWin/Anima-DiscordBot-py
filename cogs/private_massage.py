import disnake
from disnake.ext import commands

class Private_massage(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'Bot Loaded | private_massage.py ✅')

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
        owner = await self.bot.fetch_user(guild.owner_id)
        await owner.send(f"Привет, я бот **{self.bot.user.name}**! Спасибо, что добавили меня на свой сервер!\n"
                         f"Мой префикс - `!`\n"
                         f"Чтобы узнать список моих команд, напишите `.help`")

def setup(bot):
    bot.add_cog(Private_massage(bot))