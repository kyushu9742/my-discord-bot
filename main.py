import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ログイン成功: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 環境変数からトークンを取得して起動
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)

