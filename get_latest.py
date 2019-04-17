#!/usr/bin/python3

import re
import urllib.request

URL_STUDIO_HOME = 'https://developer.android.com/studio/index.html'


def get_latest_studio_url():
    with urllib.request.urlopen(URL_STUDIO_HOME) as response:
        html = response.read().decode()

    matched = re.findall('"((https)?://.*linux.tar.gz)"', html)
    # Ensure unique and then convert to a list of easy access.
    links = list(set(matched))

    if len(links) == 0:
        raise ValueError('Url matching our query not found.')
    elif len(links) > 1:
        raise RuntimeError('Multiple urls found, expected only one, urls are: {}'.format(
            ' '.join(links)))

    url = links[0][0]
    version = url.split('/')[-2]
    return version, url


if __name__ == '__main__':
    print(' '.join(get_latest_studio_url()))
