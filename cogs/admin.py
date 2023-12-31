import disnake
from disnake.ext import commands
import random
import json

nikita = 429562004399980546

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | admin.py ✅')

    @commands.slash_command(name="add_anime", description="Добавить новое аниме в список")
    async def add_anime(self, interaction, name: str, link: str):
        if interaction.user.id == nikita:
            with open('jsons/anime.json', 'r', encoding='utf-8') as f:
                anime_list = json.load(f)
            new_anime = {"name": name, "link": link}
            anime_list.append(new_anime)
            with open('jsons/anime.json', 'w', encoding='utf-8') as f:
                json.dump(anime_list, f, ensure_ascii=False, indent=4)

            await interaction.response.send_message(f'Аниме "{name}" успешно добавлено в список!')
        else:
            await interaction.response.send_message(f'Это команда предназначена для основателя бота :3', ephemeral=True)


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server_id = 984079879802876035
        channel_id = 1179439390095843358

        server = self.bot.get_guild(server_id)
        channelid = server.get_channel(channel_id)

        embed = disnake.Embed(title="Хозяин, меня пригласили на сервер, ура ура!", description=f"Название сервера **{guild.name}**", color=0xd469ff)
        embed.add_field(name="Пригласил пользователь", value=f"{guild.owner.mention} ID: {guild.owner.id} ({guild.owner.name})", inline=True)
        if guild.me.guild_permissions.create_instant_invite:
            invite = await channelid.create_invite()
            embed.add_field(name="Ссылка на сервер:", value=f"{invite}", inline=False)
        if guild.icon is not None:
            embed.set_thumbnail(url=guild.icon.url)
        await channelid.send(embed=embed)

    @commands.slash_command(name="prefix", description="Устанавливает новый префикс на вашем сервере")
    @commands.has_permissions(administrator=True)
    async def prefix(self, interaction, prefix: str):
        server_id = interaction.guild.id

        with open('jsons/prefix.json', 'r', encoding='utf-8') as f:
            prefix_list = json.load(f)

        existing_entry = next((entry for entry in prefix_list if str(entry["serverId"]) == str(server_id)), None)

        if existing_entry:
            existing_entry["prefix"] = prefix
            embed = disnake.Embed(title="Префикс успешно обновлен!", description=f'Префикс для сервера **{interaction.guild.name}** обновлен на [**{prefix}**]', color=0x00ff00)
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.set_image(url="https://media.tenor.com/F1CtXH8w6JIAAAAd/sono-bisque-doll-wa-koi-wo-soru-love-you.gif")
            embed.set_footer(text=f"Префикс обновлён администратором {interaction.user.name}")
            await interaction.response.send_message(embed=embed)
        else:
            new_prefix = {"serverId": server_id, "prefix": prefix}
            prefix_list.append(new_prefix)
            embed = disnake.Embed(title="Префикс успешно добавлен!", description=f'Префикс на сервере **{interaction.guild.name}** установлен на [**{prefix}**]', color=0x00ff00)
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.set_image(url="https://media.tenor.com/F1CtXH8w6JIAAAAd/sono-bisque-doll-wa-koi-wo-soru-love-you.gif")
            embed.set_footer(text=f"Префикс обновлён администратором {interaction.user.name}")
            await interaction.response.send_message(embed=embed)
        with open('jsons/prefix.json', 'w', encoding='utf-8') as f:
            json.dump(prefix_list, f, ensure_ascii=False, indent=4)

    @commands.slash_command(name="add_custom", description="Добавить новою кастом гифку в список")
    async def add_custom(self, interaction, name: str, link: str):
        if interaction.user.id == nikita:
            file_path = f'jsons/custom/{name}.json'

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    custom_list = json.load(f)
            except FileNotFoundError:
                custom_list = []

            if link not in custom_list:
                custom_list.append(link)

                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(custom_list, f, ensure_ascii=False, indent=4)

                embed = disnake.Embed(title=f'Гиф успешно добавлен в список **{name}**!', color=0x00ff00)
                embed.set_image(url=link)
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message(f'Гиф "{link}" уже есть в списке {name}!', ephemeral=True)
        else:
            await interaction.response.send_message(f'Эта команда предназначена для основателя бота :3', ephemeral=True)

    @commands.slash_command(name="loggs", description="Команда для добавления сервера и канала для логов")
    async def loggs(self, interaction):
        if not interaction.author.guild_permissions.administrator:
            await interaction.response.send_message("Для выполнения команды нужны права администратора.",ephemeral=True)
        else:
            server_id = interaction.guild.id
            channel_id = interaction.channel.id

            with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
                loggs_channels_list = json.load(f)
            for log_channel in loggs_channels_list:
                if log_channel["serverId"] == server_id:
                    await interaction.response.send_message(f'Логи для сервера {server_id} уже установлены!\nЕсли хотите изменить/удалить канал логов, используйте команду /deloggs', ephemeral=True)
                    return
            new_log_channel = {"serverId": server_id, "logChannelId": channel_id}
            loggs_channels_list.append(new_log_channel)

            with open('jsons/loggs.json', 'w', encoding='utf-8') as f:
                json.dump(loggs_channels_list, f, ensure_ascii=False, indent=4)

            embed = disnake.Embed(title="Логи для сервера успешно установлены! Юхуу!", color=0x00ff00)
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.add_field(name="Сервер:", value=interaction.guild.name, inline=False)
            embed.add_field(name="Канал:", value=interaction.channel.name, inline=False)
            embed.add_field(name="Как убрать запись логов?", value="Введите команду /deloggs в любом канале вашего сервера.", inline=False)
            embed.set_footer(text=f"Администратор {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="deloggs", description="Команда для удаления настроек логов на сервере")
    async def deloggs(self, interaction):
        if not interaction.author.guild_permissions.administrator:
            await interaction.response.send_message("У вас недостаточно прав для выполнения этой команды.",ephemeral=True)
            return
        server_id = interaction.guild.id
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)
        found_channel = None
        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == server_id:
                found_channel = log_channel
                break
        if found_channel is not None:
            loggs_channels_list.remove(found_channel)
            with open('jsons/loggs.json', 'w', encoding='utf-8') as f:
                json.dump(loggs_channels_list, f, ensure_ascii=False, indent=4)
            await interaction.response.send_message(f'Логи для сервера {server_id} успешно удалены!', ephemeral=True)
        else:
            await interaction.response.send_message(f'Логи для сервера {server_id} не найдены.', ephemeral=True)




def setup(bot):
    bot.add_cog(Admin(bot))