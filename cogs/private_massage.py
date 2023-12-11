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
    
    site_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Веб-сайт", url="https://github.com/NeckitWin/Anima-bot-discord")
    invite_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Пригласить бота", url="https://discord.com/api/oauth2/authorize?client_id=1165781260203986994&permissions=8&scope=bot")
    support_button = disnake.ui.Button(style=disnake.ButtonStyle.gray, label="Сервер поддержки", url="https://discord.gg/XZRQDUuKf7")
    
    view = disnake.ui.View()
    view.add_item(site_button)
    view.add_item(invite_button)
    view.add_item(support_button)

    await owner.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Private_massage(bot))