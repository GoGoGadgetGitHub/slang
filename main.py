import discord
from bot_logic import gen_pass, dice_roll
from discord.ext import commands

# intents variable stores the permissions of the bot
intents = discord.Intents.default()

# Enable the permission to read message content
intents.message_content = True

# Create a bot and pass the intents
bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def password(ctx, length:int):
    await ctx.send(gen_pass(length))

@bot.command()
async def dice(ctx):
    await ctx.send(dice_roll())

bot.run("SECRET TOKEN")
