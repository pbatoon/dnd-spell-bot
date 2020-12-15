# main.py
import os
import requests
import json
from lib import list_info
from lib.embed import DiscordEmbed
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Fetch Discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set command prefix
bot = commands.Bot(command_prefix='!')


@bot.command(name='dnd-spells', help='Responds with info about the specified spell')
async def dnd_spells(ctx, search_str, *args):
    # Format search string for api call
    formatted = str(search_str).replace(' ', '-').lower()
    url = "https://www.dnd5eapi.co/api/spells/{}".format(formatted)

    # GET request
    response = requests.get(url)
    response_text = response.text  # Convert to text

    # Tell the user when they input a spell that doesn't exist
    if response.status_code == 404:
        await ctx.send("Spell not found!")

    # Parse get request into dictionary
    data = json.loads(response_text)

    # Delete index and url entries - not necessary
    list_info.delete_info(data)

    # Initialize output
    output_list = []

    if "-damage" in args:
        await ctx.send(list_info.list_damage(data))
    elif not args:
        await ctx.send(list_info.list_all(data))

    # output = lib.list_all(data)

    # print(output)

    # await ctx.send(output)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Wrong message format!')


bot.run(TOKEN)
