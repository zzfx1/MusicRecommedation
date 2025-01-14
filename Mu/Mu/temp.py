import os

import requests


def save_cache(uid, val, filetype):
    re = requests.get(url=val)
    try:
        os.remove(str(uid) + '.' + filetype)
    except:
        pass
    with open(str(uid) + '.' + filetype, mode='wb') as f:
        for chunk in re.iter_content(512):
            f.write(chunk)
    return {'file': open(str(uid) + '.' + filetype, 'rb')}
