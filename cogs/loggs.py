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

def setup(bot):
    bot.add_cog(Loggs(bot))