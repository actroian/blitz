import playsong as p
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '+help':
        msg = "Hello! I am blitz... here are my commands:\n"
        cmds = "`+play/+p <songname>/<youtube url> //plays song or adds to queue\n+skip //plays next song in queue\n+disconnect //kick me out of voice channel`"
        return msg + cmds  # + "\nBegin a query with '?' to have a private response"

    if p_message[0:4] == '+play':
        p.play(p_message[5:])
        if True:
            return "`Now playing: " + p_message + "`"[5:]
        else:
            return "`" + p_message[5:] + " added to queue`"

    if p_message == '+skip':
        return "feature coming soon!"

    if p_message == '+disconnect':
        return "feature coming soon!"
