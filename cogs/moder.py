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
        if amount < 0:
            await interaction.response.send_message("Нельзя удалять отрицательное количество сообщений", ephemeral=True)
        elif amount > 100:
            await interaction.response.send_message("Нельзя удалять больше 100 сообщений за раз в целях безопасности", ephemeral=True)
        else:
            await interaction.channel.purge(limit=amount + 1)
            await interaction.response.send_message(f"Удалено {amount} сообщений", ephemeral=True)
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("У вас нет прав на использование этой команды", ephemeral=True)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Укажите количество сообщений для удаления", ephemeral=True)
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Укажите количество сообщений для удаления", ephemeral=True)
        else:
            await ctx.send("Произошла неизвестная ошибка", ephemeral=True)

def setup(bot):
    bot.add_cog(Moder(bot))