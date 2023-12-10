import disnake
from disnake.ext import commands

class Img(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | img.py ✅')

    @commands.command(name="sticker", description="Выводит изображение стикера, на который ответил пользователь", aliases=["stick", "стикер"])
    async def sticker(self, ctx):
        if ctx.message.reference is None:
            await ctx.send("Нужно ответить на сообщение, чтобы я могла показать стикер")
        else:
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            if len(message.stickers) == 0:
                await ctx.send("В сообщении, на которое вы ответили, нет стикеров")
            else:
                if message.stickers[0].format == disnake.StickerFormatType.png:
                    sticker_url = message.stickers[0].url
                    await ctx.send(sticker_url)
                elif message.stickers[0].format == disnake.StickerFormatType.gif:
                    sticker_url = message.stickers[0].id
                    await ctx.send(f"https://media.discordapp.net/stickers/{sticker_url}.gif")
                else:
                    await ctx.send("Формат стикера неизвестен")

    @commands.command(name="emoji", description="Выводит изображение эмодзи")
    async def emoji(self, ctx, emoji: disnake.Emoji):
        await ctx.send(emoji.url)

    # @commands.command(name="emoji_upload", description="Загружает эмодзи на сервер")
    # @commands.has_permissions(manage_emojis=True)
    # async def emoji_upload(self, ctx, emoji: disnake.Emoji):
    #     # Проверяем, есть ли у бота права управления эмодзи на сервере
    #     if not ctx.guild.me.guild_permissions.manage_emojis:
    #         await ctx.send("У меня нет прав на управление эмодзи на этом сервере.")
    #         return
    #
    #     # Создаем эмодзи на сервере
    #     try:
    #         await ctx.guild.create_custom_emoji(name=emoji.name, image=await emoji.read())
    #         await ctx.send(f"Эмодзи {emoji} успешно загружено на сервер.")
    #     except disnake.errors.HTTPException as e:
    #         await ctx.send(f"Ошибка при загрузке эмодзи: {e}")

def setup(bot):
    bot.add_cog(Img(bot))