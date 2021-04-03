# Comment créé des intégrations (embed) discord | Level : Medium

import discord
from discord.ext import commands


client = commands.Bot(command_prefix = "*")


@client.command()
async def displayembed():
	"""
	Commande pour créé des intégrations, vous pourrez ensuite la modifier à votre guise
	"""
	embed = discord.Embed(
		title = 'Title', # On ajoute le titre
		description = 'THis is a description.', # Une description
		colour = discord.Colour.blue() # la couleur de l'intéfration qui sera afficher sur la partie verticale gauche
	)

	embed.set_footer(text='This is a footer.')
	# Le bas de page de votre intégration
	embed.set_image(url='Image')
	# Warning | oublier pas de rentrer l'URL de l'image en question que vous voulez ajouter,
	# Celle-ci n'est pas obligatoire, vous pouvez ajouter une intégration sans image
	embed.set_author(name='Author Name',
	# Vous pouvez ajouter le auteur de l'intégration, elle n'est pas non plus obligatoire
	icon_url='Image')
	# Vous permet d'ajouter une petite image en tant que icon, même chose que 'embed.set_image', ajouter juste un URL
	embed.add_field(name='Field Name', value'Field Value', inline=False)
	# Un champ de texte, les valeur entre '' peuvent être modifier à votre guise
	embed.add_field(name='Field Name', value'Field Value', inline=True)
	# En revanche le 'inline=' permet de savoir si vous voulez que les champ soit aligner
	embed.add_field(name='Field Name', value'Field Value', inline=True)

	await ctx.send(embed=embed) # Puis la commande pour afficher le tous


client.run(os.getenv('TOKEN'))


# Discord Link : https://discord.com/developers/docs/intro
# Author : Fell#1679 | Add me one discord for help, I'm Free and Cool