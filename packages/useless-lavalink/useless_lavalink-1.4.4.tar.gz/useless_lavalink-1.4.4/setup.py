# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lavalink']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp', 'discord.py>=1.7,<3']

extras_require = \
{'docs': ['sphinx>=3.4.2,<5',
          'sphinx-rtd-theme>=1.0,<2.0',
          'sphinxcontrib-trio>=1.1.2,<2.0.0',
          'typing-extensions>=4.1.1,<5.0.0']}

setup_kwargs = {
    'name': 'useless-lavalink',
    'version': '1.4.4',
    'description': 'A fork of Red-Lavalink for useless_bot',
    'long_description': '# Useless Lavalink\n\n[![Build\nStatus](https://github.com/MRvillager/useless_lavalink/actions/workflows/publish_pypi.yml/badge.svg)](https://github.com/MRvillager/useless_lavalink/actions/workflows/publish_pypi.yml)\n[![Test\nStatus](https://github.com/MRvillager/useless_lavalink/actions/workflows/tests.yml/badge.svg)](https://github.com/MRvillager/useless_lavalink/actions/workflows/tests.yml)\n[![Documentation\nStatus](https://readthedocs.org/projects/useless-lavalink/badge/?version=stable)](https://useless-lavalink.readthedocs.io/en/stable/)\n\nA Lavalink client library written for Python 3.9 and 3.10 using the AsyncIO\nframework. This is a fork of\n[Red-Lavalink](https://github.com/Cog-Creators/Red-Lavalink) optimized to work with Useless Bot.\n\nTo install:\n``` bash\npip install useless_lavalink\n```\n\n# Usage\n\n``` python\nimport lavalink\nfrom discord.ext.commands import Bot\n\nbot = Bot()\n\n\n@bot.event\nasync def on_ready():\n    await lavalink.initialize(bot)\n    await lavalink.add_node(\n        bot, host=\'localhost\', password=\'password\',  ws_port=2333\n    )\n\n\nasync def search_and_play(voice_channel, search_terms):\n    player = await lavalink.connect(voice_channel)\n    tracks = await player.search_yt(search_terms)\n    player.add(tracks[0])\n    await player.play()\n```\n\n# Shuffling\n\n``` python\ndef shuffle_queue(player_id, forced=True):\n    player = lavalink.get_player(player_id)\n    if not forced:\n        player.maybe_shuffle(sticky_songs=0)\n        """\n        `player.maybe_shuffle` respects `player.shuffle`\n        And will only shuffle if `player.shuffle` is True.\n\n        `player.maybe_shuffle` should be called every time\n        you would expect the queue to be shuffled.\n\n        `sticky_songs=0` will shuffle every song in the queue.\n        """\n    else:\n        player.force_shuffle(sticky_songs=3)\n        """\n        `player.force_shuffle` does not respect `player.shuffle`\n        And will always shuffle the queue.\n\n        `sticky_songs=3` will shuffle every song after the first 3 songs in the queue.\n        """\n```\n\nWhen shutting down, be sure to do the following:\n``` python\nawait lavalink.close(bot)\n```',
    'author': 'MRvillager',
    'author_email': 'mrvillager.dev@gmail.com',
    'maintainer': 'MRvillager',
    'maintainer_email': 'mrvillager.dev@gmail.com',
    'url': 'https://github.com/MRvillager/useless_lavalink',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
