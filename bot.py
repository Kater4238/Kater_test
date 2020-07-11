import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(731447956724776980)
    await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(731470362621247489)
    await channel.send(f'{member} Leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")

bot.run("NzMxNDQ4Njk0OTUxNjQxMjIw.XwmpTA.CpC0rg3EkFipjeNAsPjXPLdfo1Y")