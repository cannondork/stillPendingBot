import discord
import random
import asyncio
import aiohttp
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands


BOT_PREFIX = ("?", "!")
TOKEN = 'NDA4NTY5NzUyMzExNTYyMjQw.DVYr0A.wvTcWnSsJvwNF-J_E9Q5dShhlg4'

client = Bot(command_prefix=BOT_PREFIX)


startup_extensions = ['Music']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

class Main_Commands():
    def __init__(self,  client):
        self.client = client


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}:  {}'.format(type(e).__name__, e)
            print('failed to load extension {}\n{}'.format(extension, exc))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(result)


@client.command()
async def add(left : float, right : float):
    """Adds two numbers together."""
    await client.say(left + right)
	
@client.command()
async def multiply(left : float, right : float):
    """Multiplies left by right."""
    await client.say(left * right)

@client.command()
async def divide(left : float, right : float):
    """Divides left by right."""
    await client.say(left / right)

@client.command()
async def minus(left : float, right : float):
    """Subtracts right from left."""
    await client.say(left - right)

    
@client.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))


client.run('NDA4NTY5NzUyMzExNTYyMjQw.DVYr0A.wvTcWnSsJvwNF-J_E9Q5dShhlg4')
