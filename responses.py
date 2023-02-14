import discord
import numpy
import os
import asyncio
import youtube_dl


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '+help':
        msg = "Hello! I am blitz... here are my commands:\n"
        cmds = "`+play/+p <songname>/<youtube url> //plays song or adds to queue\n+skip //plays next song in queue\n+disconnect //kick me out of voice channel`"
        return msg + cmds  # + "\nBegin a query with '?' to have a private response"

    if p_message[0:4] == '+play':
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
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="/opt/homebrew/Cellar/ffmpeg/5.1.2_4/bin/ffmpeg")

            # add queue system here - if queue is empty, play; else add to queue
            voice_client.play(player)

        except Exception as e:
            print(e)


        if True:
            return "`Now playing: " + p_message + "`"[5:]
        else:
            return "`" + p_message[5:] + " added to queue`"

    if p_message == '+skip':
        return "feature coming soon!"

    if p_message == '+disconnect':
        return "feature coming soon!"
