import discord


class DiscordEmbed:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def create_embed(self):
        embed = discord.Embed(title=self.title, description=self.description, color=0x5797ff)
        return embed

