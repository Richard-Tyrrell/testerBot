import discord
from discord.ext import commands
client=commands.Bot(command_prefix='#')

'''
This bot was designed to test another bots rejection of allowing it to be triggered by bots.
'''
@client.command(name='test')
async def testerino(ctx):
    if (ctx.author.bot):return
    response='This is a test of the emergency broadcast signal!'#Was testing something
    await ctx.send(response)

@client.event #testing errors
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is invalid')

@client.check #implementing no DMs
async def globally_block_dms(ctx):
    return ctx.guild is not None

client.run('Bot code redeacted for public viewing')