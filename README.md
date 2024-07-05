# Discord Notifier

This is a toy project for sending discord message to a specific channel using channel id and bot token.

## Pre-requisites
You first need to understand that discord bots are dependent to [discord developer portal](https://discord.com/developers/applications).

If you want to use bots, you'll need to register your application, make your bot and authorize it's intents, and invite the bot through oauth2 url link.

## Environment
- Python 3.10.12

## Installation

```bash
pip install -r requirements.txt
```

## Usage
Basic log function is implemented inside [functions.py](./functions.py); thus you'll only need to check *app.log* if needed.

1) Configure bot information.
You will need file named *keys.json* to specify token of bot, and channel id for bot to send message.

```json
{
    "TOKEN":"YOUR_BOT_TOKEN",
    "CHANNEL_ID":"YOUR_SERVER_TEXT_CHANNEL_ID"
}
```

2) Run bot.
*bot.py* runs as independent server.

It will use port number 10080 by default.

```bash
nohup bot.py > bot.log 2>&1 &
```

3) Run app.py with arguments.
While session running *bot.py* is alive, run *app.py* to send message.

```bash
python app.py --message "Hello World!"
```

This will send message ```Hello World!``` to your channel