from time import ctime

from gan import __version__


def run():
    cur_time = ctime()
    text = f"""
    # gan
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
