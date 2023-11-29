import disnake
from disnake.ext import commands
import random

ranime_list=[
    {"name": "Anime","link": "https://media.tenor.com/K-JwhTfkDX4AAAAM/anime-k%C4%B1z%C4%B1-anime.gif"},
    {"name": "Anime","link": "https://cdn.discordapp.com/emojis/1029984489126951680.png"},
]

class Ranime(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | ranime.py ✅')

    @commands.slash_command(name="ranime", description="Какое аниме посмотреть сегодня? :D")
    async def ranime(self, interaction):
        embed = disnake.Embed(title="Лови конфетку", color=0xff0099)
        embed.set_image(url=random.choice(ranime_list))
        embed.set_footer(text="Посоветуй меня друзьям <3")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Ranime(bot))