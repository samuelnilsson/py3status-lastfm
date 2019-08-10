# -*- coding: utf-8 -*-
"""
Displays a users currently playing track on last.fm

The username and api_key parameters are required. For the api_key, see https://www.last.fm/sv/api/authentication.

Configuration parameters:
    format: Display format (default '{artist} - {title}')
    format_stopped: Display format when nothing is playing (default 'nothing playing')
    cache_timeout: Refresh interval for this module (default 20)
    username: The username of the user to retrieve information for (default None)
    api_key: Your last.fm api key (default None)

Format placeholders:
    {artist} The currently playing artist
    {album} The currently playing album
    {title} The currently playing track title

Color options:
    color_play: A track is currently playing
    color_stop: Nothing is playing

Requires:
    requests: Python module from https://pypi.org/project/requests

@author Samuel Nilsson <samni698@gmail.com>
@license GPLv3
"""

import requests

class Py3status:

    format = '{artist} - {title}'
    format_stopped = 'nothing playing'
    cache_timeout = 20
    username = None
    api_key = None

    def __init__(self):
        self.artist = None
        self.album = None
        self.title = None

    def lastfm(self):
        if self.username is None:
            return self._create_output('Parameter username is required')
        if self.api_key is None:
            return self._create_output('Parameter api_key is required')
        try:
            song = self._get_most_recent()
        except Exception as e:
            return self._create_output(str(e))

        if song is None:
            return self._create_output(
                self.py3.safe_format(self.format_stopped),
                self.py3.COLOR_STOP
            )

        is_playing = self._is_playing(song)
        if is_playing:
            song_info = {
                'artist': song['artist']['#text'],
                'album': song['album']['#text'],
                'title': song['name']
            }
            return self._create_output(
                self.py3.safe_format(self.format, song_info),
                self.py3.COLOR_PLAY
            )
        else:
            return self._create_output(
                self.py3.safe_format(self.format_stopped),
                self.py3.COLOR_STOP
            )

    def _get_params(self):
        return {
            'api_key': self.api_key,
            'format': 'json',
            'limit': 1,
            'method': 'user.getrecenttracks',
            'user': self.username
        }

    def _get_most_recent(self):
        base_uri = 'https://ws.audioscrobbler.com/2.0/'
        params = self._get_params()

        try:
            response = requests.get(base_uri, params=params)
        except Exception:
            raise Exception('no network connection')
        if response.status_code == 200:
            response = response.json()
            if response.get('error'):
                raise Exception(response['message'])
            else:
                songs = response['recenttracks']['track']
                if len(songs) > 0:
                    return songs[0]
                else:
                    return None
        else:
            raise Exception(str(response.status_code) + str(response.reason))

    def _is_playing(self, song):
        attr = song.get('@attr')
        if not attr:
            return False
        is_playing = attr.get('nowplaying')
        return is_playing

    def _create_output(self, full_text, color=None):
        output = dict()
        output['full_text'] = full_text
        output['cached_until'] = self.py3.time_in(self.cache_timeout)
        if color:
            output['color'] = color
        return output
