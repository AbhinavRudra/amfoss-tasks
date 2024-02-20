# Invite Link : https://discord.com/api/oauth2/authorize?client_id=1196829741014077521&permissions=1084479764544&scope=bot

import discord
from scraper import *
import os
from dotenv import load_dotenv 
from discord.ext import commands
from datetime import date
import time

#Discord Token
load_dotenv()
TOKEN = os.getenv('TOKEN')

#Discord Intents
intents=discord.Intents.default()
intents.messages = True
intents.message_content = True
crickey = commands.Bot(command_prefix='!', intents=intents)

#time
today = date.today()
timestamp = time.strftime('%Y-%m-%d %H:%M:%S')


@crickey.event
async def on_ready():
    print(f'{crickey.user} is now running!')

@crickey.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Wrong command. Use `!help` to see a list of available commands.")
    
@crickey.command()
async def livescore(ctx):
    try:
        if ctx.guild is None: # Check if the command is used in a private message
            await ctx.author.send('fetching scores...')
            await ctx.author.send(team_and_score)
            await ctx.author.send(status_of_match)
            await ctx.author.send(today)
        else: # Send a message to the channel
            await ctx.channel.send('fetching scores...')
            await ctx.channel.send(team_and_score)
            await ctx.channel.send(status_of_match)
            await ctx.channel.send(today)
    except Exception as e:
        print(f"Error occurred: {e}")
        if ctx.guild is None: # Check if the command is used in a private message
            await ctx.author.send('No live scores available! Try again later.')
        else: # Send a message to the channel
            await ctx.send('No live scores available! Try again later.')
         
    add_to_csv(team_and_score)

def add_to_csv(team_and_score):
    f.write(team_and_score)
    f.write( timestamp + '\n')
    
crickey.remove_command('help')

#file handling
f = open("log.csv", "a")

@crickey.command()
async def generate(ctx):
    print("Opening logs")
    f.close()
    file = open("log.csv")
    if ctx.guild is None:
        await ctx.author.send(file=discord.File(file))
    else:
        await ctx.channel.send(file=discord.File(file))



@crickey.command()
async def help(ctx):
    print("Sending all available commands...")
    if ctx.guild is None:
        await ctx.author.send("Available Commands:")
        await ctx.author.send("!generate- get the csv file livescores are stored in")
        await ctx.author.send("!livescore- get the live scores")
    else:
        await ctx.channel.send("Available Commands:")
        await ctx.channel.send("!generate- get the csv file livescores are stored in")
        await ctx.channel.send("!livescore- get the live scores")

bot.run(TOKEN)

