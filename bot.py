import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
   print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(1114098669105451111)
   await channel.send(F'[member] join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(1114098700000690251)
   await channel.send(F'[member] leave!')

bot.run('MTA4NjE3MDY5Nzc3NDE0MTQ1MA.GOhDCX.4NeNALV7-RyfZaDQPLXPGqVqx1EGtMKNFBZcFM')
