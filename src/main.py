import json
import nextcord
from nextcord.ext import commands
import database.database as database
import logging

def load_configuration():
    try:
        with open("json/configuration.json", "r") as config:
            data = json.load(config)
            token = data["token"]
            prefix = data["prefix"]
            owner_id = data["owner_name"]
        return token, prefix, owner_id
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        return None
    except json.JSONDecodeError:
        logging.error("Error decoding configuration file.")
        return None

token, prefix, owner_id = load_configuration()

if token and prefix and owner_id:
    intents = nextcord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True
    client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

    def setup_logging():
        logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s")

    @client.event
    async def on_ready():
        database.create_table()
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=f'cross chat'))
    

    if __name__ == "__main__":
        setup_logging()
        extensions = ['cogs.cross_chat', 'cogs.setup']
        for extension in extensions:
            try:
                client.load_extension(extension)
                logging.info(f"Loaded {extension}")
            except commands.ExtensionError as e:
                logging.error(f"Failed to load {extension}: {e}")
        client.run(token)
        logging.info("Bot started")
else:
    logging.error("Failed to load configuration.")
