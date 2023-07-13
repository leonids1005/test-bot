import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utF8') as jFile:
   jdata = json.load(jFile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
   print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(int(jdata['WELCOME']))
   await channel.send(F'{member} 輕輕地來了')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(int(jdata['LEAVE']))
   await channel.send(F'{member} 輕輕地走了')

for Filename in os.listdir('./cmds'):
   if Filename.endswith('.py'):
      bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
