import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utF8') as jFile:
   jdata = json.load(jFile)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
   print(">>Bot is online<<")


@bot.command()
async def 怎麼辦(ctx):
   pic = discord.File(jdata['pic'])
   await ctx.send(file= pic)

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(int(jdata['WELCOME']))
   await channel.send(F'{member} 輕輕地來了')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(int(jdata['LEAVE']))
   await channel.send(F'{member} 輕輕地走了')

@bot.command()
async def ping(ctx):
   await ctx.send(F'{round(bot.latency*1000)} (ms)')

bot.run(jdata['TOKEN'])
