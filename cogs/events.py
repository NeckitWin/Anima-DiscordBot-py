import disnake
from disnake.ext import commands
import json
import random

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | events.py ✅')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = disnake.Embed(title=f'Добро пожаловать на сервер {member.guild.name}!', description=f'Приветики, **{member.display_name}**!\nОзнакомься с правилами сервера, и постарайся их пожалуйста не нарушать.. Няяя', color=0xcb42f5)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_image(url=random.choice(json.load(open('jsons\hi.json'))))
            await channel.send(member.mention,embed=embed)

def setup(bot):
    bot.add_cog(Events(bot))