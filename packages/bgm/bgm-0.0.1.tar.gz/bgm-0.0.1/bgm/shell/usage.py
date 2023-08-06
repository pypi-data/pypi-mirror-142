from time import ctime

from bgm import __version__


def run():
    cur_time = ctime()
    text = f"""
    # bgm
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
