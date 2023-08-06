from time import ctime

from aoe import __version__


def run():
    cur_time = ctime()
    text = f"""
    # aoe
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
