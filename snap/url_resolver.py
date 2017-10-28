#!/usr/bin/python3

import argparse
import re
import urllib.request

URL_STUDIO_HOME = 'https://developer.android.com/studio/index.html'


def get_latest_studio_url():
    with urllib.request.urlopen(URL_STUDIO_HOME) as response:
        html = response.read().decode()

    matched = re.findall('"((https)?://.*linux.zip)"', html)
    # Ensure unique and then convert to a list of easy access.
    links = list(set(matched))

    if len(links) == 0:
        raise ValueError('Url matching our query not found.')
    elif len(links) > 1:
        raise RuntimeError('Multiple urls found, expected only one, urls are: {}'.format(
            ' '.join(links)))

    return links[0][0]


def get_latest_studio_version():
    return get_latest_studio_url().split('/')[-2]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Android Studio down URL grabber.')
    parser.add_argument('output', help='Whether to print version or url.',
                        choices=['version', 'url'])
    args = parser.parse_args()
    if args.output == 'version':
        print(get_latest_studio_version())
    else:
        print(get_latest_studio_url())
