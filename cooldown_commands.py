@client.event()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown): #checks if on cooldown
		msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after) #says the time
		await ctx.send(msg) #send the error message
		#note: {:.2f} is too shorten the decimals. Example: 3.128343 would be 3.12

@client.command()
@commands.cooldown(2,10,commands.BucketType.user)
async def beg(ctx):
	await ctx.send("Someone gave you 10 coins")
