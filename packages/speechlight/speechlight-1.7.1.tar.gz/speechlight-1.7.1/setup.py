# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['speechlight']

package_data = \
{'': ['*'], 'speechlight': ['speech_libs/*']}

extras_require = \
{':platform_system == "Darwin"': ['pyobjc>=8.4,<9.0',
                                  'pyobjc-core>=8.4,<9.0',
                                  'pyobjc-framework-cocoa>=8.4,<9.0'],
 ':platform_system == "Windows"': ['pywin32>=303,<304']}

setup_kwargs = {
    'name': 'speechlight',
    'version': '1.7.1',
    'description': 'A lightweight Python library providing a common interface to multiple TTS and screen reader APIs.',
    'long_description': '# speechlight\n\nA lightweight Python library providing a common interface to multiple TTS and screen reader APIs.\n\n\n## License And Credits\n\nSpeechlight is licensed under the terms of the [Mozilla Public License, version 2.0.](https://nstockton.github.io/speechlight/license "License Page")\nSpeechlight was originally created and is actively maintained by Nick Stockton.\nmacOS support by Jacob Schmude.\n\n\n## Installation\n\n```\npip install --user speechlight\n```\n\n\n## Documentation\n\nPlease see the [API reference](https://nstockton.github.io/speechlight/api "Speechlight API Reference") for more information.\n\n\n## Example Usage\n\n```\nfrom speechlight import speech\n\n# Say something.\nspeech.say("Hello world!")\n\n# Say something else, interrupting the currently speaking text.\nspeech.say("I\'m a rood computer!", interrupt=True)\n\n# Cancel the currently speaking message.\nspeech.silence()\n\n# Braille something.\nspeech.braille("Braille dots go bump in the night.")\n\n# Speak and braille text at the same time.\nspeech.output("Read along with me.")\n\n# And to interrupt speech.\nspeech.output("Rood!", interrupt=True)\n```\n',
    'author': 'Nick Stockton',
    'author_email': 'nstockton@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nstockton/speechlight',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
