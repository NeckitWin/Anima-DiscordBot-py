import disnake
from disnake.ext import commands
import random
import json

class Ranime(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | ranime.py ✅')

    @commands.slash_command(name="ranime", description="Какое аниме посмотреть сегодня? :D")
    async def ranime(self, interaction):
        with open('jsons/anime.json', 'r', encoding='utf-8') as f:
            anime_list = json.load(f)
        random_anime = random.choice(anime_list)
        embed = disnake.Embed(title=f"Советую посмотреть", color=0xff0099)
        embed.add_field(name=f"Anime - {random_anime['name']}",value="", inline=False)
        embed.set_image(url=random_anime['link'])
        embed.set_footer(text="Посоветуй меня друзьям <3")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Ranime(bot))