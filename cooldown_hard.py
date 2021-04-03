# Comment créé un cooldown pour n'importe quel commande | Level : Hard

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

"""
@commands.cooldown(rate,per,BucketType) 
# Limit how often a command can be used, (num per, seconds, BucketType.default/user/member/guild/channel/role)
@client.command()
#Your command
"""


@client.event # WARNING | WITH NO ()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #checks if on cooldown
        msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after) #says the time
        await ctx.send(msg) #send the error message
        #note: {:.2f} is too shorten the decimals. Example: 3.128343 would be 3.12


#---------------------------------------------------------------------------------------------

# Example 1 :

@client.command()
async def cooldowntest1(ctx):
	await ctx.send('I have no cooldown. Which means i can be spammed!')

# That is your current command
# Lets change it now.

@client.command()
@commands.cooldown(1, 10, commands.Bucket.user)  # I have a cooldown of 10 seconds. Per user.
# You can replace user with guild/member/default
async def cooldowntest2(ctx):
	await ctx.send('I have a cooldown. Which means i cant be spammed!')

# To increase or decrease your cooldown just simple change the numbers 1, 10.
# However if you want your cooldown to target a different subject :
#  Use the command r!rtfm BucketType in a Bot commands channel!


#---------------------------------------------------------------------------------------------

# Example 2 :

@client.command()
@commands.cooldown(2,10,commands.BucketType.user)
async def beg(ctx):
	await ctx.send("Someone gave you 10 coins")


client.run('TOKEN')

# Video Version Tuto : https://www.youtube.com/watch?v=7hJwNAMOP0k
# Discord Link : https://discord.com/developers/docs/intro
# Author : Fell#1679 | Add me one discord for help, I'm Free and Cool
