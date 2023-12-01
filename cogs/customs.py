import disnake
from disnake.ext import commands
import random
import json

class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot Loaded | custom.py ✅')

    @commands.slash_command(name="kiss", description="Выберите, кого поцеловать из участников сервера")
    async def kiss(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Сладкий поцелуй", description=f"Вас поцеловал участник {ctx.author.mention}, вы в смущении 0,0", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\kiss.json'))))
        await ctx.send(member.mention,embed=embed)

    @commands.slash_command(name="pat", description="Выберите, кого погладить из участников сервера")
    async def pat(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Гладь гладь", description=f"Вас погладил участник {ctx.author.mention}, вам стало приятно)", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\pat.json'))))
        await ctx.send(member.mention,embed=embed)

    @commands.slash_command(name="hug", description="Выберите, кого обнять из участников сервера")
    async def hug(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Я тебя сожму!", description=f"Вас обнял участник {ctx.author.mention}, это было мило :)", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\hug.json'))))
        await ctx.send(member.mention,embed=embed)

    @commands.slash_command(name="cry", description="Покажите, что вам грустно")
    async def cry(self, ctx):
        embed = disnake.Embed(title="Мне очень грустно", description=f"Участник {ctx.author.mention} заплакал((", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\cry.json'))))
        await ctx.send(embed=embed)

    @commands.slash_command(name="bite", description="Выберите, кого укусить из участников сервера")
    async def bite(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Смачный укус", description=f"Вас укусил участник {ctx.author.mention}, у вас остался след от зубов...", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\\bite.json'))))
        await ctx.send(member.mention,embed=embed)

    @commands.slash_command(name="hit", description="Выберите, кого ударить из участников сервера")
    async def hit(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Мощный удар!", description=f"Вас ударил участник {ctx.author.mention}, вам очень больно..", color=ctx.author.color)
        embed.set_image(url=random.choice(json.load(open('jsons\custom\hit.json'))))
        await ctx.send(member.mention,embed=embed)


def setup(bot):
    bot.add_cog(Custom(bot))