import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from discord.ext import commands

# --- Renderのポート監視（無料Web Service化）対策 ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# バックグラウンドで簡易サーバーを起動
threading.Thread(target=run_server, daemon=True).start()

# --- Discord Bot本体 ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ログイン成功: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
