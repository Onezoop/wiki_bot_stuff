import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

with open("TOKEN.txt", 'r') as txt:
    TOKEN = txt.read()

@client.event
async def on_ready():
    print(f'regular bot {client.user} online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(message.content)
        print(message)





client.run(TOKEN)
