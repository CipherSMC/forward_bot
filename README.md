# forward_bot
Credit: https://www.instructables.com/Create-a-Free-Telegram-Auto-Forward-Application-fo/

# Linux Install
To run the Forward_Bot, install the Python library <b>telethon</b> on your Linux system.

```console
sudo pip install telethon
```

```python
from telethon import TelegramClient, events
import asyncio
import logging
from telethon.tl import functions, types  # Import the necessary types/functions
logging.basicConfig(level=logging.WARNING)
import random  # Import the random module to introduce randomness to the delay

# Replace these values with your own api_id and api_hash
api_id = 123456789
api_hash = '123456789123456789'

# Provide the folder path for the session
session_path = "/home/ciphersmc/Auto_Foreward_Bot"

# Initialize the TelegramClient
client = TelegramClient(session_path, api_id, api_hash)
client.start()

# From Channnel 1
from_ch1 = 123
to_channelforward1 = 456

# From Channnel 2
from_ch2 = 123
to_channelforward2 = 456

# From Channnel 3
from_ch3 = 123
to_channelforward3 = 456

# From Channnel 4
from_ch4 = 123
to_channelforward4 = 456

# From Channnel 5
from_ch5 = 123
to_channelforward5 = 456

# From Channnel ....
from_ch.... = 123
to_channelforward.... = 456


# Function to send a message with a random delay
async def send_message_with_delay(client, chat_id, message):
    # Generate a random delay between 5 to 20 seconds
    delay = random.uniform(5, 20)
    await asyncio.sleep(delay)
    try:
    	# Use default timeout values provided by Telethon
        await client.send_message(chat_id, message)
    except Exception as e:
        logging.warning(f"Failed to send message: {e}")

# Function to forwad a message with a random delay
async def forward_message_with_delay(client, chat_id, message):
    # Generate a random delay between 5 to 20 seconds
    delay = random.uniform(5, 20)
    await asyncio.sleep(delay)
    try:
    	# Use default timeout values provided by Telethon
        await client.forward_messages(chat_id, message)
    except Exception as e:
        logging.warning(f"Failed to forward message: {e}")

# Your event handler function
@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()

    # Handle different chats here
    if chat.id == from_ch1:
        await send_message_with_delay(client, to_channelforward1, event.message)

    if chat.id == from_ch2:
        await send_message_with_delay(client, to_channelforward2, event.message)

    if chat.id == from_ch3:
        await send_message_with_delay(client, to_channelforward3, event.message)

    if chat.id == from_....:
        await forward_message_with_delay(client, to_....., event.message)

asyncio.get_event_loop().run_forever()
```
