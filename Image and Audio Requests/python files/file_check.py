def format_check(link):
    """
    Checks the format of the file from a file request link and returns it

    :parameter:
    link (str): Desired link using for file request

    :returns:
    The Image / Audio format verified

    """
    if '.png' in link:
        return '.png'
    elif '.jpg' in link:
        return '.jpg'
    elif '.jpeg' in link:
        return '.jpeg'
    elif '.gif' in link:
        return '.gif'
    elif '.mp3' in link:
        return '.mp3'
    elif '.flac' in link:
        return '.flac'
