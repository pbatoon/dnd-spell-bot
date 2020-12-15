# main.py
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands

# Fetch Discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set command prefix
bot = commands.Bot(command_prefix='!')


@bot.command(name='dnd-spells', help='Responds with info about the specified spell')
async def dnd_spells(ctx, search_str):
    # Format search string for api call
    formatted = str(search_str).replace(' ', '-').lower()
    url = "https://www.dnd5eapi.co/api/spells/{}".format(formatted)

    # GET request
    response = requests.get(url)
    response_text = response.text       # Convert to text

    # Tell the user when they input a spell that doesn't exist
    if response.status_code == 404:
        await ctx.send("Spell not found!")

    # Parse get request into dictionary
    data = json.loads(response_text)

    # Delete index and url entries - not necessary
    del data['index']
    del data['url']

    # Initialize output
    output_list = []

    for key, value in data.items():
        # Capitalize first letter in every key to make the output more presentable.
        cap_key = key.replace('_', ' ').capitalize()

        # If the value of the key isn't a list or a dictionary, straight up print it
        if not isinstance(value, list) and not isinstance(value, dict):
            out_string = f"**{cap_key}:** {value}"
            output_list.append(out_string)
        # If the value is a list but only consists of one thing, print it
        elif isinstance(value, list) and len(value) == 1 and isinstance(value[0], str):
            out_string = f"**{cap_key}:** {value[0]}"
            output_list.append(out_string)
        # For the 'components' value ONLY
        elif key == 'components':
            c_string = f"**{cap_key}:** " + ', '.join([str(c) for c in value])

            # Replace the one-letter abbreviations with long form.
            out_string = c_string.replace("V", "Verbal").replace("S", "Somatic").replace("M", "Material")

            output_list.append(out_string)

    output = '\n'.join([str(i) for i in output_list])

    # print(output)

    await ctx.send(output)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Wrong message format!')


bot.run(TOKEN)
