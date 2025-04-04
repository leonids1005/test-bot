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
    if msg.author == bot.user:
        return  # 機器人不理自己

    target_channel_id = 1086059639340281906  

    if msg.channel.id != target_channel_id:
        return  

    if '：/' in msg.content:
        await msg.channel.send('你再傳一次試試')

    elif '？' in msg.content:
        await msg.channel.send('？')

    elif '行' in msg.content:
        await msg.channel.send('行')

    await bot.process_commands(msg)


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
