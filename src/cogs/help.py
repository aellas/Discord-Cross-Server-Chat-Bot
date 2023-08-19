import nextcord
from nextcord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(name="help", description="Help")
        
def setup(bot):
    bot.add_cog(HelpCog(bot))