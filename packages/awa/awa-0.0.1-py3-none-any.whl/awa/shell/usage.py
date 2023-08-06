from time import ctime

from awa import __version__


def run():
    cur_time = ctime()
    text = f"""
    # awa
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
