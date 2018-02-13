import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]
bot = commands.Bot("?")


@bot.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

class Main_Commands():
    def __init__(self,  bot):
        self.bot = bot

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}:  {}'.format(type(e).__name__, e)
            print('failed to load extension {}\n{}'.format(extension, exc))


bot.run('NDA4NTY5NzUyMzExNTYyMjQw.DVYr0A.wvTcWnSsJvwNF-J_E9Q5dShhlg4')
