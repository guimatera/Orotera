# Importando pacotes necessários
import discord
from discord.ext import commands
import os
import sys


# Credenciais 
Token = open(os.path.join(os.path.dirname(sys.argv[0]),'credential.txt')).read()

# Prefixo de comando estabelecido
bot = commands.Bot(command_prefix='%')

# Mostra que o Bot foi inicializado
@bot.event
async def on_ready():
    print("Current Bot connected: {}" .format(bot.user.name))
    print("Bot ID: {}" .format(bot.user.id))


# Bot rodando
bot.run(Token)







