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

    embed = disnake.Embed(title=f"Привет, я бот **{self.bot.user.name}**!", description=(f"Спасибо, что добавили меня на свой сервер!\n"
      f"Мой префикс - `!`\n"
      f"Чтобы узнать список моих команд, напишите `.help`"), color=0xc0c0c0)
    embed.set_thumbnail(url=self.bot.user.display_avatar.url)
    
    site_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Веб-сайт", custom_id="buttonSite")
    invite_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Пригласить бота", custom_id="buttonInvite")
    support_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Сервер поддержки", custom_id="buttonSupport")

    #button_functuonal or Class
    
    view = disnake.ui.View()
    view.add_item(site_button)
    view.add_item(invite_button)
    view.add_item(support_button)

    await owner.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Private_massage(bot))