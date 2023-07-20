import nextcord
from nextcord.ext import commands
import database.database as database
import sqlite3

class SetupCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @nextcord.slash_command(name="setup_channel", description="Setup Channel ID")
    async def add_channel(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel):
        await interaction.response.send_message(f"You have set <#{channel.id}> as your advertising channel")
        sqlite3.connect("src/database/channel_ids.db")
        database.add_channel_id(channel.id)
    
    @nextcord.slash_command(name="remove_channel", description="Remove Channel ID")
    async def remove_channel(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel):
        await interaction.response.send_message(f"You have removed <#{channel.id}> as your advertising channel")
        database.remove_channel_id(channel.id)

def setup(bot):
    bot.add_cog(SetupCog(bot))