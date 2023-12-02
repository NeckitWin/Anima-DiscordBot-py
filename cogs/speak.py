import disnake
from disnake.ext import commands
import random
import json

class Speak(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | speak.py ✅')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if "приветики" in message.content.lower():
            await message.channel.send(f"Приветствую, {message.author.mention}!")
        elif "тест" in message.content.lower():
            await message.channel.send(f"Я работаю, всё хорошо!")
        elif "анима" in message.content.lower():
            await message.channel.send(random.choice(json.load(open('jsons/ask.json', encoding='utf-8'))))

def setup(bot):
    bot.add_cog(Speak(bot))