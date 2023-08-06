from time import ctime

from cnm import __version__


def run():
    cur_time = ctime()
    text = f"""
    # cnm
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
