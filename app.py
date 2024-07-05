import argparse, pathlib, os, json, asyncio, aiohttp
from functions import log

BASEDIR = pathlib.Path(__file__).parent.resolve()

async def main(args):
    url = "http://localhost:10080/send_message"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "channel_id": keys["CHANNEL_ID"],
        "message": args.message
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            log(await response.text())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send message to Discord bot.")
    parser.add_argument('--message', type=str, required=True, help='Message to send to Discord bot')

    args = parser.parse_args()

    keypath = os.path.join(BASEDIR, "./keys.json")
    with open(keypath, "r") as f:
        keys = json.load(f)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args))
