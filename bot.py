import discord
import responses
import bottoken
import numpy
import os
import asyncio
import youtube_dl

async def send_message(message, user_message, isPrivate):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_bot():
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
        p_message = user_message.lower()
        print(f"{username} said: '{user_message}' in {channel}")

        if p_message.startswith('+play'):
            try:
                src = p_message.split()[1]

                voice_clients = {}
                yt_dl_opts = {'format': 'best-audio/best'}
                ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

                ffmpeg_options = {'options': '-vn'}
                voice_client = await message.author.voice.channel.connect()
                voice_clients[voice_client.guild.id] = voice_client

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(src, download=False))

                song = data['src']
                player = discord.FFmpegPCMAudio(song, **ffmpeg_options,
                                                executable="/opt/homebrew/Cellar/ffmpeg/5.1.2_4/bin/ffmpeg")

                # add queue system here - if queue is empty, play; else add to queue
                voice_client.play(player)

            except Exception as e:
                print(e)

            #if True:
            #    return "`Now playing: " + p_message + "`"[5:]
            #else:
            #    return "`" + p_message[5:] + " added to queue`"

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, isPrivate=True)

        else:
            await send_message(message, user_message, isPrivate=False)

    client.run(bottoken.T)
