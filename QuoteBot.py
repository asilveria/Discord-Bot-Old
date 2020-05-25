#quoting bot
#import os
import random
import discord
from discord.ext import commands
#from dotenv import load_dotenv
import json

"""

"""

quotedata = {}
quotedata['quotes'] = []
quotedata['quotes'].append({
    'name': 'CheesyFajitas',
    'quote': 'This is a test quote.',
    'date': '5/25/2020'
})

with open('quotes.txt','w') as outfile:
    json.dump(quotedata,outfile,indent=4,)

#load_dotenv('.env')
TOKEN = 'NjU4MDE0OTEyMDE4MjUxNzc3.XspEKA.8NABn78_NPBXbGgD_4obsLPNpvM'
GUILD = 'The Triangle of Trust'

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='quote', help='Responds with a random quote add via server users')
async def grabQuote(ctx):
    jsonDump = json.dumps(quotedata)

    await ctx.send()
@bot.command()
async def addquote(ctx,*,arg):
    #coolPeopleQuotes.append(arg)
    await ctx.send(arg)

bot.run(TOKEN)
