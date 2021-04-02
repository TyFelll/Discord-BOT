# Comment créé son propre bot discord | La Base de Base | Level : Very Easy

import discord
from discord.ext import commands
# On importe les modules principaux

client = commands.Bot(command_prefix = "*") # Remplacer '*' par ce que vous voulez | Ce sera le(s) caractère(s) nécessaire avant toutes commandes

@client.event() # C'est un des décorators qui vous permet de activer une fonction
async def on_ready():
	"""
	Cette fonction vous permet d'envoyer un message dans la console 'Ready' quand le bot est prêt
	Elle permet aussi au bot de lui ajouter un statue 'Watching', sur 'Netflix'
	"""
	print("Ready") # Renvoi 'Ready' a la console
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "Netflix"))
	# Vous pouvez aussi modifier le 'watching' par playing/streaming/listening
	# Le name= 'Netflix', est modifiable a votre guise

client.run('TOKEN') # Oublier pas de modifier votre TOKEN par celui de votre bot | Le TOKEN est le code secret de votre bot

# Link : https://discord.com/developers/docs/intro
# Author : Fell#1679 | Add me one discord for help, I'm Free and Cool
