import os
import discord
import random
from discord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix='!')

#Quote command
@bot.command()
async def quote(ctx):
  quotes = open("quotes.txt", "r")
  lines = quotes.read()
  list_of_quotes = lines.splitlines()
  quotes.close()
  
  i = random.randint(0,len(list_of_quotes)-1)
  await ctx.send(list_of_quotes[i])

#Compliment command
@bot.command()
async def compliment(ctx, member: discord.Member):
  compliments = open("compliments.txt", "r")
  lines = compliments.read()
  list_of_compliments = lines.splitlines()
  compliments.close()
  
  i = random.randint(0,len(list_of_compliments)-1)
  await ctx.send(list_of_compliments[i] + " " + str(member.name) + '!')

#Magic 8 ball command
@bot.command()
async def magic8(ctx):
  responses = open("8ballresponses.txt", "r")
  lines = responses.read()
  list_of_responses = lines.splitlines()
  responses.close()
  
  i = random.randint(0,len(list_of_responses)-1)
  await ctx.send("The magic 8 ball says: " + list_of_responses[i])

#Tater easter egg command
@bot.command()
async def tater(ctx):
  await ctx.send("tot!")

#Yogi easter egg command
@bot.command()
async def yogi(ctx):
  await ctx.send("WE LOVE THE FLUFFY YOGI BEAR!")

@bot.command()
async def choose(ctx, *choices : str):
    choice=random.choice(choices)
    await ctx.send("I choose: " + choice)
  
#Hug command
@bot.command()
async def hug(ctx, member: discord.Member):
  await ctx.send(ctx.author.name + " gives a massive hug to " + member.name)

my_secret = os.environ['TOKEN']

keep_alive()
bot.run(my_secret)
