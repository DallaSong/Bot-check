from discord.ext import commands
import discord, asyncio
import os
import levelsys
import webserver

cogs = [levelsys]

print("hell0o")
i = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents = i)

async def load():
  for i in range(len(cogs)):
    await cogs[i].setup(client)

@client.event
async def on_ready():
  print("Bot is ready")
  print(f"Logged in as {client.user}")
  await load()



async def main():
  async with client:
    await client.start(os.environ['TOKEN'])

asyncio.run(main())

webserver.keep_alive()