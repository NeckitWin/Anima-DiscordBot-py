import disnake
from disnake.ext import commands

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | play.py ✅')

    @commands.command()
    async def play(self, ctx):
        embed = disnake.Embed(title="Ты хочешь играть?", description="Нажми на кнопку ниже", color=0x00ff00)
        embed.set_thumbnail(url=ctx.author.display_avatar.url)

        async def yes_button_callback(interaction: disnake.MessageInteraction):
            # Создаем новый Embed
            new_embed = disnake.Embed(title="Ты в игре!", description="Приготовься к веселью!", color=0xffd700)
            new_embed.set_thumbnail(url=ctx.author.display_avatar.url)

            # Отправляем новый Embed
            await interaction.response.edit_message(embed=new_embed)

            # Здесь вы можете добавить ваш код для выполнения действий после нажатия "Да"

        yes_button = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Да")
        yes_button.callback = yes_button_callback

        no_button = disnake.ui.Button(style=disnake.ButtonStyle.red, label="Нет")

        view = disnake.ui.View()
        view.add_item(yes_button)
        view.add_item(no_button)

        await ctx.send(embed=embed, view=view)


def setup(bot):
    bot.add_cog(Play(bot))