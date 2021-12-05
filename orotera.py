# Importando pacotes necessários
import discord
from discord.ext import commands

# Credenciais
Token = "OTE2NzA2MjU4NjU0OTg2Mjgw.YauDOw.9qMaYiF71_v6BrATEV3on0QoAeo"

# Prefixo de comando estabelecido
bot = commands.Bot(command_prefix='%')

# Mostra que o Bot foi inicializado
@bot.event
async def on_ready():
    print("Current Bot connected: {}" .format(bot.user.name))
    print("Bot ID: {}" .format(bot.user.id))


# Bot rodando
bot.run(Token)







