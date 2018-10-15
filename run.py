import discord
from discord.ext import commands

TOKEN = 'NDg5Nzg4MDQxNTg2ODAyNjg4.DoQHcw.2fowZDgciJL3PTu2kTTF2vxrky4'

client=commands.Bot(command_prefix = 'alexa ')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output)














































client.run(TOKEN)
