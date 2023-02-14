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

    if p_message == '+skip':
        return "feature coming soon!"

    if p_message == '+disconnect':
        return "feature coming soon!"
