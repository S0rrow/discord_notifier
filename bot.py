import discord, asyncio, json, pathlib, os
from discord.ext import commands
from aiohttp import web
from functions import log, bot, send_message

# global
BASEDIR = pathlib.Path(__file__).parent.resolve()
keypath = os.path.join(BASEDIR, "./keys.json")
with open(keypath, "r") as f:
    keys = json.load(f)
    
@bot.event
async def on_ready():
    log(f'Logged in as {bot.user.name}', 2)
    print(f'Logged in as {bot.user.name}')

async def handle_message(request):
    data = await request.json()
    channel_id = data.get('channel_id')
    message = data.get('message')
    
    if channel_id and message:
        await send_message(channel_id, message)
        return web.Response(text="Message sent")
    else:
        return web.Response(text="Invalid data", status=400)

app = web.Application()
app.router.add_post('/send_message', handle_message)

async def start_http_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 10080)
    await site.start()

async def run_bot(token):
    await start_http_server()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.close()
    except Exception as e:
        log(f"Bot encountered an error: {e}", 1)
        await bot.close()

if __name__ == "__main__":
    token = keys["TOKEN"]
    asyncio.run(run_bot(token))
