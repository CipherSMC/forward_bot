# Import necessary libraries, including telethon.tl functions and types
from telethon import TelegramClient, events
import asyncio
import logging
import os

# Set up logging to see warnings
logging.basicConfig(level=logging.WARNING)

# Replace your API credentials and session name
api_id = 12345678
api_hash = '12345678'
session_name = "your_session_name"

# Determine the directory of your script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the session file path
session_path = os.path.join(script_dir, session_name)

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

# Define retry constants
max_retries = 5  # Maximum number of retries
base_delay = 5  # Initial retry delay in seconds

# Create a list to store messages
message_queue = []

# Function to send or forward a message with a retry strategy
async def send_or_forward_message(client, chat_id, message):
    retry_delay = base_delay
    retries = 0

    while retries < max_retries:
        try:
	    # Send the message to the destination chat
	    await client.send_message(chat_id, message)
            return  # Message sent/forwarded successfully
        except Exception as e:
            retries += 1
            logging.warning(f"Failed to send message (attempt {retries}): {e}")
            await asyncio.sleep(retry_delay)
            retry_delay *= 2  # Implement exponential backoff

    logging.warning("Max retries reached. Could not send/forward the message.")

# Function to process messages from the queue
async def process_messages_from_queue(client):
    while message_queue:
        chat_id, message = message_queue.pop(0)
        await send_or_forward_message(client, chat_id, message)

# Define an event handler for new messages
@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()

    # Based on the source chat, add messages to the queue
    if chat.id == from_ch1:
        message_queue.append((to_channelforward1, event.message))

    if chat.id == from_ch2:
        message_queue.append((to_channelforward2, event.message))

    if chat.id == from_ch3:
        message_queue.append((to_channelforward3, event.message))


# Schedule a periodic task to send/forward messages from the queue
async def send_or_forward_messages_periodically(client):
    while True:
        await process_messages_from_queue(client)
        await asyncio.sleep(60)  # Process messages every 1 minute (adjust as needed)

# Start the task for periodic message processing
asyncio.get_event_loop().create_task(send_or_forward_messages_periodically(client))

# Start the event loop
asyncio.get_event_loop().run_forever()
