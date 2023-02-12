import discord
import responses
import token

async def send_message(message, user_message, isPrivate):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = token.T
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user: #makes sure whatever bot says isnt input back into bot
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, isPrivate=True)

        else:
            await send_message(message, user_message, isPrivate=False)

    client.run(TOKEN)
