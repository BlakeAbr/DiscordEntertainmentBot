from typing import Final
from discord import Intents, Client, Message
from responses import get_response

#Important to keep secret
TOKEN: Final[str] = "YOUR DISCORD BOT TOKEN"

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


#Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message.startswith('?'):
        return  # Do nothing if the message does not start with ?

    # Removes the ? from the beginning of the message
    user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Message handling
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#States if the bot has come online
@client.event
async def on_ready() -> None:
    channel = client.get_channel(YOUR CHANNEL ID) #Channel ID will change per server
    if channel:
        await channel.send(f'{client.user} is now online. Try ?help for some fun commands') #Gives basic introduction of what the bot can do
    print(f'{client.user} is now online.')


def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()