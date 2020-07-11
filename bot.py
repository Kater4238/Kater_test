import discord
from discord.ext import commands
import json
import random

with open('setting.json','r') as j_file:
    j_data = json.load(j_file)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>> Bot is online <<')
    
'''
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(j_data['Welcome_channel']))
    await channel.send(f'{member} 滑入MHW的世界!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(j_data['Leave_channel']))
    await channel.send(f'{member} 掉出MHW世界!')
'''

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def pic(ctx):
    random_pic = random.choice(j_data['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

bot.run(j_data['TOKEN'])