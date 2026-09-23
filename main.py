import discord
from discord.ext import commands

TOKEN = "MTU1MjIyNDU5MjE2NzMwNTI3Ng.GNnzlA.lBVKPz6KfeEPUJgjR253FGZGuLVQcTAWM3rIKk"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def testjanus(ctx):
    await ctx.send("@everyone @here\n𝙹𝙰𝙽𝚄𝚂 𝙽𝙿𝙲 𝙷𝙰𝚂 𝚂𝙿𝙰𝚆𝙽𝙴𝙳! 𝙶𝙴𝚃 𝙸𝙽 𝙷𝙴𝚁𝙴 𝙰𝚂𝙰𝙿!")

bot.run(TOKEN)
