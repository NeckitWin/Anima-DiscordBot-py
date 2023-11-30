import disnake
from disnake.ext import commands

class Moder(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | moder.py ✅')

    @commands.slash_command(name="clear", description="Очистка чата")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, interaction: disnake.ApplicationCommandInteraction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Удалено {amount} сообщений пользователем {interaction.user.name}")

def setup(bot):
    bot.add_cog(Moder(bot))