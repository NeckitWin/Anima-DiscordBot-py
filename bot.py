import os
import json

import disnake
from disnake.ext import commands

with open('token.json', 'r') as f:
    token = json.load(f)

token = token.get('token')

intents=disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

admin = 993270145302667307

@bot.event
async def on_ready():
    print('Я успешно запустилась!')
    await bot.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name=f'/help',type=disnake.ActivityType.watching))

@bot.command()
@commands.has_role(admin)
async def reload(ctx, extension):
    extension = extension.lower()
    if f'cogs.{extension}' in bot.extensions:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} перезагружен')
    else:
        await ctx.send(f'{extension} не установлен либо не был загружен')
@bot.command()
@commands.has_role(admin)
async def unload(ctx, extension):
    extension = extension.lower()
    if f'cogs.{extension}' in bot.extensions:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} отгружен')
    else:
        await ctx.send(f'{extension} не установлен либо не был загружен')

@bot.command()
async def reload_all(ctx):
    if ctx.author.top_role.id != admin:
        await ctx.send('Команда доступна только для основателя бота')
    else:
        for cog in list(bot.extensions):
            bot.unload_extension(cog)
            bot.load_extension(cog)
        await ctx.send('Все коги перезагружены')

@bot.slash_command(name='reload_all', description='Перезагрузить все коги (доступно только владельцу бота)')
async def reload_all(ctx):
    if ctx.author.top_role.id != admin:
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