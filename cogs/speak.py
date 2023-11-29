from disnake.ext import commands

class Speak(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | speak.py ✅')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Проверка, что сообщение отправлено не ботом, чтобы избежать зацикливания
        if message.author.bot:
            return
        if "привет" in message.content.lower():
            await message.channel.send(f"Приветствую, {message.author.mention}!")

def setup(bot):
    bot.add_cog(Speak(bot))