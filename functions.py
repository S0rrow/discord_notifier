import os
import pathlib
import discord
from time import localtime, strftime
from discord.ext import commands

BASEDIR = pathlib.Path(__file__).parent.resolve()

def log(msg, flag=None):
    if flag is None:
        flag = 0

    head = ["debug", "error", "status"]
    now = strftime("%H:%M:%S", localtime())
    logpath = os.path.join(BASEDIR, "./app.log")

    try:
        with open(logpath, "a") as logfile:
            logfile.write(f"[{now}][{head[flag]}] > {msg}\n")
    except Exception as e:
        print(f"exception on log function: {e}")

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())

async def send_message(channel_id, message):
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        log(f"Channel with ID {channel_id} not found.", 1)
        try:
            channel = await bot.fetch_channel(channel_id)
            await channel.send(message)
            log(f"message sent to {channel_id}: {message}", 2)
        except Exception as e:
            log(f"Failed to fetch channel with ID {channel_id}: {e}", 1)
