# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quizli']

package_data = \
{'': ['*']}

install_requires = \
['rich>=11.0.0,<12.0.0', 'typer-cli>=0.0.12,<0.0.13']

entry_points = \
{'console_scripts': ['quizli = quizli.main:app']}

setup_kwargs = {
    'name': 'quizli',
    'version': '1.0.0',
    'description': 'An educational project teaching how to open-source an interactive Python quiz app',
    'long_description': "![Logo](https://github.com/pwenker/quizli/blob/main/docs/assets/logo.png?raw=true)\n\n_An educational project teaching how to open-source an interactive Python quiz app_\n\n|  | quizli |\n| --- | --- |\n| Project Stats               | [![GitHub Repo stars](https://img.shields.io/github/stars/pwenker/quizli?style=social)](https://github.com/pwenker/quizli) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pwenker/quizli) ![Lines of code](https://img.shields.io/tokei/lines/github/pwenker/quizli)\n| Documentation | [![User Guide](https://img.shields.io/badge/docs-User%20Guide-brightgreen)](https://pwenker.github.io/quizli/user_guide) [![Learning Guide](https://img.shields.io/badge/docs-Learning%20Guide-brightgreen)](https://pwenker.github.io/quizli/learning_guide/) [![Demos](https://img.shields.io/badge/docs-Showcase-brightgreen)](https://pwenker.github.io/quizli/demos.html) |\n| Build status                  | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pwenker/quizli/test_package) ![Codecov](https://img.shields.io/codecov/c/github/pwenker/quizli) |\n| Activity & Issue Tracking | ![GitHub last commit](https://img.shields.io/github/last-commit/pwenker/quizli) [![GitHub issues](https://img.shields.io/github/issues-raw/pwenker/quizli)](https://github.com/pwenker/quizli/issues?q=is%3Aopen+is%3Aissue) [![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/pwenker/quizli)](https://github.com/pwenker/quizli/issues?q=is%3Aissue+is%3Aclosed)  |\n| PyPI                      | [![PyPI](https://img.shields.io/pypi/v/quizli)](https://pypi.org/project/quizli/)                                                                                                                                  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/quizli) [![Downloads](https://pepy.tech/badge/quizli/month)](https://pepy.tech/project/quizli)|\n| News & Updates | [![Twitter Follow](https://img.shields.io/twitter/follow/PascalWenker?style=social)](https://twitter.com/PascalWenker) [![GitHub followers](https://img.shields.io/github/followers/pwenker?style=social)](https://github.com/pwenker)|\n\n## Demo\n\n[![asciicast](https://asciinema.org/a/474148.svg)](https://asciinema.org/a/474148)\n\n## :mortar_board: Learning Guide\n\nThis guide teaches you how to effectively share a Python app with the open-source community.\n\n|  | Learning Guide |\n| --- | --- |\nInteractive quiz app| [How to create an interactive Python quiz app?](https://pwenker.github.io/quizli/learning_guide/quiz.html)\nCommand Line Interface | [How to add a CLI to your quiz app?](https://pwenker.github.io/quizli/learning_guide/cli.html)\nDocumentation | [How to create a slick documentation for your app?](https://pwenker.github.io/quizli/learning_guide/documentation.html)\nPublishing | [How to build, manage and publish your Python package to PyPi?](https://pwenker.github.io/quizli/learning_guide/publishing.html)\nTesting | [How to test your app?](https://pwenker.github.io/quizli/learning_guide/testing.html)\n\n## :rocket: User Guide\n\nThis guide contains usage and reference material for the `quizli` app.\n\n|  | User Guide |\n| --- | --- |\nCLI Reference | [Usage & reference for `quizli's` CLI](https://pwenker.github.io/quizli/user_guide/cli.html)\nCode Reference | [Usage & reference for `quizli's` source code](https://pwenker.github.io/quizli/code_reference/index.html)\n\n\n## Quickstart\n\n### :package: Installation\n\nInstall quizli with [`pip`](https://pip.pypa.io/en/stable/getting-started/):\n\n```console\npip install quizli\n```\n\n### :zap: Entrypoint\nTo get help about `quizli's` commands open your console and type:\n\n```console\nquizli --help\n```\n\nThe same works for subcommands, e.g. :\n\n```console\nquizli demo --help\n```\n",
    'author': 'Pascal Wenker',
    'author_email': 'pwenker@posteo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pwenker/quizli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
