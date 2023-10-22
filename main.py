import discord
import os, random
import requests
from settings import settings 
from bot_logic import *
from discord.ext import commands
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


# def get_duck_image_url():    
#     url = 'https://random-d.uk/api/random'
#     res = requests.get(url)
#     data = res.json()
#     return data['url']


# @bot.command('duck')
# async def duck(ctx):
#     '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
#     image_url = get_duck_image_url()
#     await ctx.send(image_url)


# @bot.command()
# async def hello(ctx):
#     await ctx.send(f'Cześć, jestem bot {bot.user}')

# @bot.command()
# async def heh(ctx, count_heh=5):
#     await ctx.send('he' * count_heh)
    
# @bot.command()
# async def mem(ctx):
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
    
#     await ctx.send(file=picture)





@bot.command(name='sortuj')
async def sortuj_smieci(ctx, przedmiot):
    przedmiot = przedmiot.lower()
    kategorie = {
        'papier': 'Do pojemnika na papier!',
        'szkło': 'Do pojemnika na szkło!',
        'plastik': 'Do pojemnika na plastik!',
        'bio': 'Do pojemnika na bioodpady!',
        'inne': 'Do pojemnika na odpady ogólnego użytku!',
    }

    if przedmiot in kategorie:
        await ctx.send(kategorie[przedmiot])
    else:
        await ctx.send('Nie jestem pewny, gdzie powinno się wyrzucić ten przedmiot.')





decomposition_data = {
    'plastik': 'około 500 lat',
    'szkło': 'około 1 milion lat',
    'papier': 'około 2-5 miesięcy',
    'bio': 'około 1-6 miesięcy',
    'metal': 'około 50-200 lat',
}

@bot.command(name='rozklad')
async def rozklad(ctx, przedmiot):
    przedmiot = przedmiot.lower()
    if przedmiot in decomposition_data:
        czas_rozkładu = decomposition_data[przedmiot]
        await ctx.send(f'{przedmiot.capitalize()} rozkłada się: {czas_rozkładu}')
    else:
        await ctx.send('Nie znaleziono informacji o rozkładzie tego przedmiotu.')





damage_data = {
    'plastik': 'Wysoka szkodliwość dla środowiska, nie ulega rozkładowi.',
    'szkło': 'Niska szkodliwość, ulega rozkładowi w około 1 milion lat.',
    'papier': 'Średnia szkodliwość, rozkłada się w około 2-5 miesięcy.',
    'bio': 'Niska szkodliwość, rozkłada się w około 1-6 miesięcy.',
    'metal': 'Średnia szkodliwość, rozkłada się w około 50-200 lat.',
}

@bot.command(name='szkodliwosc')
async def szkodliwosc(ctx, przedmiot):
    przedmiot = przedmiot.lower()
    if przedmiot in damage_data:
        informacje = damage_data[przedmiot]
        await ctx.send(f'{przedmiot.capitalize()} przenosi szkody dla środowiska: {informacje}')
    else:
        await ctx.send('Nie znaleziono informacji o szkodliwości tego przedmiotu.')

    
bot.run(settings['TOKEN'])




