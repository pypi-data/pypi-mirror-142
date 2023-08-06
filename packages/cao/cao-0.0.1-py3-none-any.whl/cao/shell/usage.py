from time import ctime

from cao import __version__


def run():
    cur_time = ctime()
    text = f"""
    # cao
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
