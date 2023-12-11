import disnake
from disnake.ext import commands
import datetime

class Private_massage(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'Bot Loaded | private_massage.py ✅')

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    owner = await self.bot.fetch_user(guild.owner_id)

    embed = disnake.Embed(title=f"**Спасибо за приглашение!**",description=(f"На данный момент меня можно настроить с помощью команд, но очень скоро появится удобная панель управления для настройки вашего прекрасного сервера.\n\nЧтобы узнать о доступных командах, используйте `/help` или посетите наш сайт."), color=0xc0c0c0)
    embed.set_thumbnail(url=self.bot.user.display_avatar.url)
    embed.set_footer(text=f"{guild.name} | {datetime.datetime.now()}", icon_url=guild.icon.url)
    
    site_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Веб-сайт", custom_id="buttonSite", url="https://anima-bot.xyz/")
    invite_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Пригласить бота", custom_id="buttonInvite")
    support_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Сервер поддержки", custom_id="buttonSupport")
    
    view = disnake.ui.View()
    view.add_item(site_button)
    view.add_item(invite_button)
    view.add_item(support_button)

    await owner.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Private_massage(bot))