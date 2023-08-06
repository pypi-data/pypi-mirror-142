import hashlib
from configparser import ConfigParser
from functools import partial
from os import path
from pathlib import Path
from re import match

configfilename = '.nasminerrc'

configfile = path.expanduser(f'~/{configfilename}')
config = ConfigParser()
config.read(configfile)


def calcmd5(filename):
    chunksize = 2 ** 29  # 512 MiB
    md5hash = hashlib.md5()
    with open(filename, mode='rb') as f:
        readchunk = partial(f.read, chunksize)
        for chunk in iter(readchunk, b''):
            md5hash.update(chunk)
    return md5hash.hexdigest()


def getLocation(filepath):
    parts = Path(filepath).parent.parts
    for part in reversed(parts):
        res = __match_location(part)
        if res:
            break
    else:
        return None
    return res


def __match_location(part):
    pattern_bmt = r'BO ?(\d+)'
    m = match(pattern_bmt, part)
    if m:
        val = int(m[1])
        return f'BO{val:02}'

    pattern_bot1 = r'BOT ?(\d|$)'
    m = match(pattern_bot1, part)
    if m:
        val = m[1]
        val = int(val) if val else 0
        return f'BOT{val}'

    # Ortho BO3   Ortho SAS1
    pattern_bot2 = r'Ortho ?(BO|SAS)(\d)'
    m = match(pattern_bot2, part)
    if m:
        if m[1] == 'SAS':
            val = f'SAS{m[2]}'
        else:
            val = m[2]
        return f'BOT{val}'

    # Mater BO1   Mater BO2
    pattern_mater = r'Mater ?BO(\d)'
    m = match(pattern_mater, part)
    if m:
        return f'MATER{m[1]}'

    if 'sspi' in part.lower():
        return 'SSPI'

    if 'dechoc' in part.lower() or 'edf ect' in part.lower():
        return 'DECHOC'

    if 'ortho' in part.lower():
        return 'BOT0'

    pattern_nri = r'.*(R[56]|R0[56])'
    m = match(pattern_nri, part)
    if m:
        return f'R{m[1][-1]}'

    if 'endoscopie' in part.lower():
        return 'ENDOS'

    return None
