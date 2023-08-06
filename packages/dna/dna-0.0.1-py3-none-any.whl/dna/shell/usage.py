from time import ctime

from dna import __version__


def run():
    cur_time = ctime()
    text = f"""
    # dna
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
