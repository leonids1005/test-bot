import discord
From discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready()
   print(">>Bot is online<<")

@bot.event
async def on_member_join(member)
   channel = bot.get_channel()
   await channel.send(F'[member] join')

@bot.event
async def on_member_remove(member)
   print(F'[member] leave')

   bot.run(MTA4NjE3MDY5Nzc3NDE0MTQ1MA.G35fy6.JmLajaT2kCdyclopFVDAGeruQCoQsOwPB45wt4)
