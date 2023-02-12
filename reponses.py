def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '+help':
        msg = "Hello! I am blitz... here are my commands:\n"
        cmds = "`+play/+p <songname>/<youtube url> //plays song or adds to queue\n+skip //plays next song in queue\n+disconnect //kick me out of voice channel`"
        return msg + cmds  # + "\nBegin a query with '?' to have a private response"

    if p_message[0:4] == '+play':
        return "coming soon!"

    if p_message == '+skip':
        return "coming soon!"

    if p_message == '+disconnect':
        return "coming soon!"
