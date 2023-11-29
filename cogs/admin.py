import disnake
from disnake.ext import commands
import random
import json

admin = 993270145302667307

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | admin.py ✅')

    @commands.slash_command(name="add_anime", description="Добавить новое аниме в список")
    @commands.has_role(admin)
    async def add_anime(self, interaction, name: str, link: str):
        with open('jsons/anime.json', 'r', encoding='utf-8') as f:
            anime_list = json.load(f)
        new_anime = {"name": name, "link": link}
        anime_list.append(new_anime)
        with open('jsons/anime.json', 'w', encoding='utf-8') as f:
            json.dump(anime_list, f, ensure_ascii=False, indent=4)

        await interaction.response.send_message(f'Аниме "{name}" успешно добавлено в список!')

def setup(bot):
    bot.add_cog(Admin(bot))