# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['signalbot', 'signalbot.utils']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.9.1,<4.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'redis>=4.1.4,<5.0.0',
 'websockets>=10.2,<11.0']

setup_kwargs = {
    'name': 'signalbot',
    'version': '0.5.5',
    'description': 'Framework to create your own Signal bots',
    'long_description': '# Signal Bot Framework\n\nPython package to build your own Signal bots. To run the the bot you need to start the [signal-cli-rest-api](https://github.com/bbernhard/signal-cli-rest-api) service and link your device with it. Please refer to that project for more details. The API server must run in `json-rpc` mode.\n\n## Classes and API\n\n*Documentation work in progress. Feel free to open an issue for questions.*\n\nThe package provides methods to easily listen for incoming messages and responding or reacting on them. It also provides a class to develop new commands which then can be registered within the bot.\n\n### Signalbot\n\n- `bot.listen(group_id, group_secret)`: Listen for messages in a group. `group_secret` must be prefixed with `group.`\n- `bot.register(command)`: Register a new command\n- `bot.start()`: Start the bot\n- `bot.send(receiver, text, listen=False)`: Send a new message\n- `bot.react(message, emoji)`: React to a message\n- `bot.start_typing(receiver)`: Start typing\n- `bot.stop_typing(receiver)`: Stop typing\n- `bot.scheduler`: APScheduler > AsyncIOScheduler, see [here](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/asyncio.html?highlight=AsyncIOScheduler#apscheduler.schedulers.asyncio.AsyncIOScheduler)\n- `bot.storage`: In-memory or Redis stroage, see `storage.py`\n\n### Command\n\nTo implement your own commands, you need to inherent `Command` and overwrite following methods:\n\n- `setup(self)`: Start any task that requires to send messages already, optional\n- `describe(self)`: String to describe your command, optional\n- `handle(self, c: Context)`: Handle an incoming message. By default, any command will read any incoming message. `Context` can be used to easily reply (`c.send(text)`), react (`c.react(emoji)`) and to type in a group (`c.start_typing()` and `c.stop_typing()`). You can use the `@triggered` decorator to listen for specific commands or you can inspect `c.message.text`.\n\n### Unit Testing\n\nIn many cases, we can mock receiving and sending messages to speed up development time. To do so, you can use `signalbot.utils.ChatTestCase` which sets up a "skeleton" bot. Then, you can send messages using the `@chat` decorator in `signalbot.utils` like this:\n```python\nclass PingChatTest(ChatTestCase):\n    def setUp(self):\n        # initialize self.singal_bot\n        super().setUp()\n        # all that is left to do is to register the commands that you want to test\n        self.signal_bot.register(PingCommand())\n\n    @chat("ping", "ping")\n    async def test_ping(self, query, replies, reactions):\n        self.assertEqual(replies.call_count, 2)\n        for recipient, message in replies.results():\n            self.assertEqual(recipient, ChatTestCase.group_secret)\n            self.assertEqual(message, "pong")\n```\nIn `signalbot.utils`, check out `ReceiveMessagesMock`, `SendMessagesMock` and `ReactMessageMock` to learn more about their API.\n\n## Getting Started\n\n*Todo, see https://github.com/filipre/signalbot-example*\n\n## Troubleshooting\n\n- Check that you linked your account successfully\n- Is the API server running in `json-rpc` mode?\n- Can you receive messages using `wscat` (websockets) and send messages using `curl` (http)?\n- Do you see incoming messages in the API logs?\n- Do you see the "raw" messages in the bot\'s logs?\n- Do you see "consumers" picking up jobs and handling incoming messages?\n- Do you see the response in the bot\'s logs?\n\n## Local development and package\n\n*Section WIP*\n\n```\npoetry install\n\npoetry run pre-commit install\n\npoetry shell\n\npoetry version\npoetry version <new_version>\n\npoetry config repositories.testpypi https://test.pypi.org/legacy/\npoetry config http-basic.testpypi __token__ <token>\npoetry config http-basic.pypi __token__ <token>\n\npoetry publish -r testpypi\npoetry publish\n```\n\n## Other Projects\n\n|Project|Description|Language|Status|\n|-------|-----------|--------|------|\n|https://github.com/signalapp/libsignal-service-java|Signal Library|Java|Last change 12 Nov 2019|\n|https://github.com/AsamK/signal-cli|A CLI and D-Bus interface for Signal|Java|active, build on top of https://github.com/signalapp/libsignal-service-java|\n|https://github.com/bbernhard/signal-cli-rest-api|REST API Wrapper for Signal CLI|Go|active, build on top of https://github.com/AsamK/signal-cli|\n|https://github.com/aaronetz/signal-bot|Bot Framework|Java|Last change 18 Feb 2021|\n|https://github.com/signal-bot/signal-bot|Bot Framework|Python|Last change 6 Jul 2018|\n',
    'author': 'René Filip',
    'author_email': None,
    'maintainer': 'René Filip',
    'maintainer_email': None,
    'url': 'https://github.com/filipre/signalbot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
