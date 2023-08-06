# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_blocklist',
 'django_blocklist.management',
 'django_blocklist.management.commands',
 'django_blocklist.migrations',
 'django_blocklist.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2,<4.0']

setup_kwargs = {
    'name': 'django-blocklist',
    'version': '1.0.1',
    'description': 'A Django app that implements IP-based blocklisting.',
    'long_description': '# Django-blocklist\nA Django app that implements IP-based blocklisting. It consists of a data model for the blocklist entries, and middleware that performs the blocking. It is mostly controlled by its management commands.\n\nThis app is primarily intended for use in situations where server-level blocking is not available, e.g. on platform-as-a-service hosts like PythonAnywhere or Heroku. Being an application-layer solution, it\'s not as performant as blocking via firewall or web server process, but is suitable for moderate traffic sites. It also offers better integration with the application stack, for easier management.\n\n## Quick start\n1. Add "blocklist" to your INSTALLED_APPS setting like this::\n\n        INSTALLED_APPS = [\n        ...\n        "blocklist"\n        ]\n\n2. Add the middleware like this::\n\n       MIDDLEWARE = [\n           ...\n          "blocklist.middleware.BlocklistMiddleware"\n       ]\n\n3. Customize settings (optional)::\n\n       BLOCKLIST_CONFIG = {\n           "cooldown": 1,  # Days to expire, default 7\n           "cache-ttl": 120,  # Seconds that utils functions cache the full list, default 60\n           "denial-template": "Your IP address {ip} has been blocked for violating our Terms of Service. IP will be unblocked after {cooldown} days."\n         }\n\n4. Run `python manage.py migrate` to create the `blocklist_blockedip` table.\n5. Add IPs to the list (via management commands,  `utils.add_to_blocklist`, or the admin).\n\n## Management commands\nDjango-blocklist includes several management commands:\n\n* `add_to_blocklist` &mdash; (one or more IPs)\n* `remove_from_blocklist` &mdash; (one or more IPs)\n* `search_blocklist` &mdash; look for an IP in the list; in addition to info on stdout, returns an exit code of 0 if successful\n* `update_blocklist` &mdash; change the `reason` or `cooldown` values for existing entries\n* `import_blocklist` &mdash; convenience command for importing IPs from a file\n* `report_blocklist` &mdash; information on the current entries\n* `clean_blocklist` &mdash; remove entries that have fulfilled their cooldown period\n\nThe `--help` for each of these details its available options.\n\nFor exporting or importing BlockedIP entries, use Django\'s built-in `dumpdata` and `loaddata` management commands.\n\n## Reporting\nThe `report_blocklist` command gives information about the current collection of IPs, including:\n* Number of listed IPs\n* Total number of blocked requests from listed IPs\n* Number of IPs active in last 24 hours\n* Number of stale IPs (added over 24h ago and not seen since)\n* Five IPs with highest block count\n* Five IPs most recently blocked\n* Longest running entry\n* IP counts by reason\n\n## Utility methods\nThe `utils` module defines two convenience functions for updating the list from your application code:\n* `add_to_blocklist(ips: set, reason="")` adds IPs to the blocklist\n* `remove_from_blocklist(ip: str)` removes an entry, returning `True` if successful',
    'author': 'Paul Bissex',
    'author_email': 'paul@bissex.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
