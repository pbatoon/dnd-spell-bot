import discord


class DiscordEmbed:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.embed = discord.Embed(title=title, description=description, color=0x5797ff)