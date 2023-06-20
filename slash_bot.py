import wiki_functions
import discord
bot = discord.Bot()

with open("TOKEN.txt", 'r') as txt:
    TOKEN = txt.read()

@bot.event
async def on_ready():
    print(f"slash commands {bot.user} online")

@bot.slash_command(guild_ids=[1101746959276052612])
async def wiki_search(ctx, user_input:str):
    await ctx.respond(wiki_functions.return_a_pageurl(user_input), ephemeral=True)


bot.run(TOKEN)
