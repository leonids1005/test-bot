import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utF8') as jFile:
   jdata = json.load(jFile)

class React(Cog_Extension):

    @commands.command()
    async def 怎麼辦(self,ctx):
       pic = discord.File(jdata['pic'])
       await ctx.send(file= pic)

    @commands.command()
    async def how(self, ctx):
       random_pic = random.choice(jdata['how'])
       how = discord.File(random_pic)
       await ctx.send(file= how)

    @commands.command()
    async def anime(seif, ctx):
       random_pic = random.choice(jdata['url_pic'])
       await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))