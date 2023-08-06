# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_uff']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.1.12,<4.0.0', 'pyperclip>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['git-uff = git_uff.main:main']}

setup_kwargs = {
    'name': 'git-uff',
    'version': '0.3.0',
    'description': 'Prints the forge url for a given file of a Git repository checkout',
    'long_description': '# git-uff\n\nPrints the forge URL for a given file of a Git repository checkout.\n\n## Intro\n\nHave you ever been discussing with colleagues over IRC/Slack/Matrix/whatever about source code and found yourself needing to point them to a particular file in a git repository?\n\nThis is tedious to do.\n\nOne solution is to tell them the path in their checkout, hoping they are on the same branch as you.\n\nAnother solution is to point your browser to the forge hosting your git repository, select the right branch, navigate the file hierarchy, find your file and copy the file URL.\n\nA better (in my opinion 😉) solution is to use `git-uff`. This tool adds an `uff` (short for "URL for file") git sub-command, which takes the path to a file in your repository checkout and prints the matching forge URL.\n\nFor example to print the URL of the `src/linux/nanonote.desktop` file from my [Nanonote][] project:\n\n```\n$ git uff src/linux/nanonote.desktop\nhttps://github.com/agateau/nanonote/blob/master/src/linux/nanonote.desktop\n```\n\n[Nanonote]: https://github.com/agateau/nanonote\n\nYou can also point them to a specific line with the `-l` argument:\n\n```\n$ git uff src/linux/nanonote.desktop -l 10\nhttps://github.com/agateau/nanonote/blob/master/src/linux/nanonote.desktop#L10\n```\n\n`git-uff` has a few other available options. Here is its `--help` output:\n\n<!-- [[[cog\nimport subprocess\nresult = subprocess.run(["git-uff", "--help"], capture_output=True, text=True)\ncog.outl("```")\ncog.out(result.stdout)\ncog.outl("```")\n]]]-->\n```\nusage: git-uff [-h] [-b BRANCH] [-p] [-c] [-l LINE] path\n\nPrints the forge URL for a given file or path of a Git repository checkout.\n\npositional arguments:\n  path                  File for which we want the URL\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -b BRANCH, --branch BRANCH\n                        Use branch BRANCH instead of the current one\n  -p, --permalink       Replace the branch in the URL with the commit it\n                        points to\n  -c, --copy            Copy the result to the clipboard\n  -l LINE, --line LINE  Line to point to\n\nNew forges can be declared in git configuration. You can do so using\n`git config`, like this:\n\n    git config --global uff.<forge_base_url>.forge <forge>\n\nWhere <forge> must be one of: cgit, github, gitlab, sourcehut.\n\nFor example to declare that example.com uses GitLab:\n\n    git config --global uff.example.com.forge gitlab\n```\n<!--[[[end]]] -->\n\n## What if my code is not on GitHub?\n\n`git-uff` is not tied to GitHub. It supports GitLab, SourceHut and CGit forges.\n\nTo declare a new forge, add it to your git configuration with:\n\n    git config --global uff.<forge_base_url>.forge <forge>\n\nFor example to declare that example.com uses GitLab:\n\n    git config --global uff.example.com.forge gitlab\n\nSee the output of `git uff --help` for the valid `<forge>` values.\n\n## Installation\n\nThe recommended method to install `git-uff` is to use [pipx][]:\n\n```\npipx install git-uff\n```\n\n[pipx]: https://github.com/pipxproject/pipx\n\nBut you can also install it with `pip`:\n\n```\npip install --user git-uff\n```\n\n## License\n\nApache 2.0\n',
    'author': 'Aurélien Gâteau',
    'author_email': 'mail@agateau.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/agateau/git-uff',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
