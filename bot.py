import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
   print(">>Bot is online<<")

   bot.run('MTA4NjE3MDY5Nzc3NDE0MTQ1MA.GOhDCX.4NeNALV7-RyfZaDQPLXPGqVqx1EGtMKNFBZcFM')
