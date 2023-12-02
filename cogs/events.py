import disnake
from disnake.ext import commands
import json
import random

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.total_counter = 0
        self.reaction_given = False
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

    # ставить рандомные emoji на новые сообщения в чатах используя эмодзи с сервера, на котором появляются сообщения, то есть надо вытащить массив эмодзи сервера
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild:
            self.total_counter += 1

            if not self.reaction_given:
                # Даем реакцию рандомно
                if random.randint(1, 20) == 20:
                    guild_emojis = message.guild.emojis
                    if guild_emojis:
                        random_emoji = random.choice(guild_emojis)
                        await message.add_reaction(random_emoji)
                    self.reaction_given = True

            if self.total_counter >= 25:
                self.total_counter = 0
                self.reaction_given = False


def setup(bot):
    bot.add_cog(Events(bot))