# py3status-lastfm
A [py3status](https://github.com/ultrabug/py3status) module for displaying a users currently playing song on last.fm

## install
Clone the repository and run
```text
pip install .
```
in the repository root.

## usage
From the module documentation:
```text
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
```
