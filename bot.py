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
async def on_message(msg):
	 if '：/' in msg.content and msg.author != bot.user:
	     await msg.channel.send('你他媽再傳一次試試看')

@bot.event
async def on_message(msg):
	 if '？' in msg.content and msg.author != bot.user:
	     await msg.channel.send('？')

@bot.command()
async def load(ctx, extension):
   bot.load_extension(F'cmds.{extension}')
   await ctx.send(F'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
   bot.unload_extension(F'cmds.{extension}')
   await ctx.send(F'Un-Loaded {extension} done.')   

@bot.command()
async def reload(ctx, extension):
   bot.reload_extension(F'cmds.{extension}')
   await ctx.send(F'Re-Loaded {extension} done.')

for Filename in os.listdir('./cmds'):
   if Filename.endswith('.py'):
      bot.load_extension(F'cmds.{Filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
