import disnake
from disnake.ext import commands
import json
import datetime

class Loggs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | loggs.py ✅')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == message.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Удалено сообщение", description=f"Содержимое сообщения: {message.content}", color=0x00ff00)
                    embed.add_field(name="Сообщение создано пользователем:", value=f"{message.author.mention} ID: {message.author.id} ({message.author.name})", inline=True)
                    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
                    embed.add_field(name="Удалено из канала:", value=message.channel.mention, inline=True)
                    embed.set_footer(text=f"Сообщение было удалено: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    async for entry in message.guild.audit_logs(limit=1, action=disnake.AuditLogAction.message_delete):
                        if entry.target.id == message.author.id:
                            embed.add_field(name="Удалено пользователем", value=f"{entry.user.mention} ID: {entry.user.id} ({entry.user.name})", inline=False)
                            break
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == before.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Изменено сообщение", description=f"Содержимое измененного сообщения:\nДо:{before.content}\nПосле:{after.content}", color=0x00ff00)
                    embed.add_field(name="Сообщение создано пользователем:", value=f"{before.author.mention} ID: {before.author.id} ({before.author.name})", inline=True)
                    embed.set_author(name=before.author.display_name, icon_url=before.author.avatar.url)
                    embed.add_field(name="Изменено в канале:", value=before.channel.mention, inline=True)
                    embed.set_footer(text=f"Сообщение было изменено: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == member.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Пользователь присоединился к серверу", color=0x00ff00)
                    embed.add_field(name="Пользователь:", value=f"{member.mention} ID: {member.id} ({member.name})", inline=True)
                    embed.set_author(name=member.display_name, icon_url=member.avatar.url)
                    embed.set_footer(text=f"Пользователь присоединился к серверу: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == member.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Пользователь покинул сервер", color=0x00ff00)
                    embed.add_field(name="Пользователь:", value=f"{member.mention} ID: {member.id} ({member.name})", inline=True)
                    embed.set_author(name=member.display_name, icon_url=member.avatar.url)
                    embed.set_footer(text=f"Пользователь покинул сервер: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Пользователь был забанен", color=0x00ff00)
                    embed.add_field(name="Пользователь:", value=f"{user.mention} ID: {user.id} ({user.name})", inline=True)
                    embed.set_author(name=user.display_name, icon_url=user.avatar.url)
                    embed.set_footer(text=f"Пользователь был забанен: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Пользователь был разбанен", color=0x00ff00)
                    embed.add_field(name="Пользователь:", value=f"{user.mention} ID: {user.id} ({user.name})", inline=True)
                    embed.set_author(name=user.display_name, icon_url=user.avatar.url)
                    embed.set_footer(text=f"Пользователь был разбанен: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == before.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    embed = disnake.Embed(title="Пользователь был обновлен", color=0x00ff00)
                    embed.add_field(name="Пользователь до:", value=f"{before.mention} ID: {before.id} ({before.name})", inline=True)
                    embed.add_field(name="Пользователь после:", value=f"{after.mention} ID: {after.id} ({after.name})", inline=True)
                    embed.set_author(name=before.display_name, icon_url=before.avatar.url)
                    embed.set_footer(text=f"Пользователь был обновлен: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        with open('jsons/loggs.json', 'r', encoding='utf-8') as f:
            loggs_channels_list = json.load(f)

        for log_channel in loggs_channels_list:
            if log_channel["serverId"] == member.guild.id:
                log_channel_id = log_channel["logChannelId"]

                channel = self.bot.get_channel(log_channel_id)
                if channel:
                    if before.channel is None and after.channel is not None:
                        embed = disnake.Embed(title="Пользователь вошел в голосовой канал", color=0x00ff00)
                        embed.add_field(name="Пользователь:", value=f"{member.mention} ID: {member.id} ({member.name})", inline=True)
                        embed.add_field(name="Канал:", value=f"{after.channel.mention} ID: {after.channel.id}", inline=True)
                        embed.set_author(name=member.display_name, icon_url=member.avatar.url)
                        embed.set_footer(text=f"Пользователь вошел в голосовой канал: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                        await channel.send(embed=embed)
                        break
                    elif before.channel is not None and after.channel is None:
                        embed = disnake.Embed(title="Пользователь вышел из голосового канала", color=0xff0000)
                        embed.add_field(name="Пользователь:", value=f"{member.mention} ID: {member.id} ({member.name})", inline=True)
                        embed.add_field(name="Канал:", value=f"{before.channel.mention} ID: {before.channel.id}", inline=True)
                        embed.set_author(name=member.display_name, icon_url=member.avatar.url)
                        embed.set_footer(text=f"Пользователь вышел из голосового канала: {datetime.datetime.now().date()} {datetime.datetime.now().time():%H:%M:%S}")
                        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Loggs(bot))