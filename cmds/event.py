import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utF8') as jFile:
   jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
       channel = self.bot.get_channel(int(jdata['WELCOME']))
       await channel.send(F'{member} 輕輕地來了')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
       channel = self.bot.get_channel(int(jdata['LEAVE']))
       await channel.send(F'{member} 輕輕地走了')

    @commands.Cog.listener()
    async def on_message(self, msg):
       if msg.content == '欸嘿':
           await msg.channel.send('你再傳一次試試')
   
def setup(bot):
    bot.add_cog(Event(bot))