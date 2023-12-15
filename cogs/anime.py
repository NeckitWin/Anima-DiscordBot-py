import disnake
from disnake.ext import commands
import random
import json

class Anime(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | anime.py ✅')

    @commands.slash_command(name="ranime", description="Посоветовать вам аниме?)")
    async def ranime(self, interaction):
        with open('jsons/anime.json', 'r', encoding='utf-8') as f:
            anime_list = json.load(f)
        random_anime = random.choice(anime_list)
        embed = disnake.Embed(title=f"Советую посмотреть Аниме", color=0xff0099)
        embed.add_field(name=f"{random_anime['name']}",value="", inline=False)
        embed.set_image(url=random_anime['link'])
        embed.set_footer(text="Посоветуй меня друзьям <3", icon_url=interaction.author.avatar.url if interaction.author.avatar else None)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Anime(bot))