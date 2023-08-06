# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_pass']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.21,<3.0']

entry_points = \
{'console_scripts': ['poetry = passwordgen:create_password']}

setup_kwargs = {
    'name': 'simple-pass',
    'version': '1.1',
    'description': 'Secure Password Generator and Checker (uses HaveIBeenPwned)',
    'long_description': '# simple-password-generation\n\nGenerate and check secure passwords in Python.\n\nThis is intended for use as a password strength checking and suggestion library for APIs, though it could also be integrated into a password database application.\n\n# Usage\n\n    >>> from simple_pass import create_password, check_havebeenpwned, scoring\n    >>> password = create_password()\n    >>> print(password)\n    unfurcate necessitate nonfact retrogradation swathband orthitic\n    \n    >>> check_havebeenpwned(password)\n    True\n    >>> scoring(password)\n    (True, 75)\n\n\n## HaveIBeenPwned\nGenerated passwords are automatically securely checked against the [HaveIBeenPwned](https://haveibeenpwned.com) database.\nPartial hashes are sent using the HaveIBeenPwned API. This can not be reconstructed to determine the checked password.\n\nUser generated passwords can be checked by calling `check_havebeenpwned(password)`.\n\n\n## Scoring Options\nPasswords can be checked with a scoring based system using the following options.\n\n    def scoring(\n        password,\n        *,\n        minimum_length=8,\n        minimum_score=20,\n        points_for_lower=2,\n        points_for_upper=2,\n        points_for_numbers=2,\n        points_per_special=2,\n        special_characters=" !@#$%^&*()-=_+.,<>[]{}/?\\\\|",\n        points_per_character=1,\n    ):\n\nI believe this scoring system encourages long and difficult to guess passwords by rewarding lengthy passwords and special characters, but without requiring a specific password format or frustrating rules.\n\n## XKCD, Comics, Horses, and batteries\n\nFor wisdom on what makes a good password see the famous [xkcd correct horse battery staple comic](https://xkcd.com/936/). The `correct horse battery staple` example passes with a score of 36 using the default parameters. It does not pass the HaveIBeenPwned check, however, as it is a well known password that has probably been found in many breaches.\n',
    'author': 'Tom Faulkner',
    'author_email': 'tomfaulkner@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TomFaulkner/simple-password-generation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
