import os
import json

import disnake
from disnake.ext import commands

with open('token.json', 'r') as f:
        token = json.load(f)

token = token.get('token')

with open('jsons/prefix.json', 'r') as f:
    prefix = json.load(f)

intents = disnake.Intents.all()

def get_prefix(bot, message):
    server_id = str(message.guild.id)
    with open('jsons/prefix.json', 'r') as f:
        prefix_list = json.load(f)

    for entry in prefix_list:
        if str(entry["serverId"]) == server_id:
            return entry["prefix"]
    return '!'

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

admin = 429562004399980546

@bot.event
async def on_ready():
    print('Я успешно запустилась!')
    await bot.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name=f'/help',type=disnake.ActivityType.watching))

@bot.command()
async def reload_all(ctx):
    if ctx.author.id != admin:
        await ctx.send('Команда доступна только для основателя бота')
    else:
        for cog in list(bot.extensions):
            bot.unload_extension(cog)
            bot.load_extension(cog)
        await ctx.send('Все коги перезагружены')

@bot.slash_command(name='reload_all', description='Перезагрузить все коги (доступно только владельцу бота)')
async def reload_all(ctx):
    if ctx.author.id != admin:
        await ctx.send('Команда доступна только для основателя бота', ephemeral=True)
    else:
        for cog in list(bot.extensions):
            bot.unload_extension(cog)
            bot.load_extension(cog)
        await ctx.send('Все коги перезагружены', ephemeral=True)

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(token)