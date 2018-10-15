import discord
from discord.ext import commands



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





client.run(config.token)
