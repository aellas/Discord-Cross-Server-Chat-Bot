
import json
import nextcord
from nextcord.ext import commands
import database.database as database

with open("src/json/configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    owner_id = data["owner_name"]

intents = nextcord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix=prefix, help_command=None, intents=nextcord.Intents.all())

@client.event
async def on_ready():
    database.create_table()
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name = f'cross chat'))
    print(f"Logged in as {client.user}")
    
extensions = [
    'cogs.cross_chat',
    'cogs.setup',
    ]

for extension in extensions:
    client.load_extension(extension)
    print(f"Loaded {extension}")
    
client.run(token)