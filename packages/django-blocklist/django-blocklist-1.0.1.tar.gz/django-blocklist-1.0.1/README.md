# Django-blocklist
A Django app that implements IP-based blocklisting. It consists of a data model for the blocklist entries, and middleware that performs the blocking. It is mostly controlled by its management commands.

This app is primarily intended for use in situations where server-level blocking is not available, e.g. on platform-as-a-service hosts like PythonAnywhere or Heroku. Being an application-layer solution, it's not as performant as blocking via firewall or web server process, but is suitable for moderate traffic sites. It also offers better integration with the application stack, for easier management.

## Quick start
1. Add "blocklist" to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = [
        ...
        "blocklist"
        ]

2. Add the middleware like this::

       MIDDLEWARE = [
           ...
          "blocklist.middleware.BlocklistMiddleware"
       ]

3. Customize settings (optional)::

       BLOCKLIST_CONFIG = {
           "cooldown": 1,  # Days to expire, default 7
           "cache-ttl": 120,  # Seconds that utils functions cache the full list, default 60
           "denial-template": "Your IP address {ip} has been blocked for violating our Terms of Service. IP will be unblocked after {cooldown} days."
         }

4. Run `python manage.py migrate` to create the `blocklist_blockedip` table.
5. Add IPs to the list (via management commands,  `utils.add_to_blocklist`, or the admin).

## Management commands
Django-blocklist includes several management commands:

* `add_to_blocklist` &mdash; (one or more IPs)
* `remove_from_blocklist` &mdash; (one or more IPs)
* `search_blocklist` &mdash; look for an IP in the list; in addition to info on stdout, returns an exit code of 0 if successful
* `update_blocklist` &mdash; change the `reason` or `cooldown` values for existing entries
* `import_blocklist` &mdash; convenience command for importing IPs from a file
* `report_blocklist` &mdash; information on the current entries
* `clean_blocklist` &mdash; remove entries that have fulfilled their cooldown period

The `--help` for each of these details its available options.

For exporting or importing BlockedIP entries, use Django's built-in `dumpdata` and `loaddata` management commands.

## Reporting
The `report_blocklist` command gives information about the current collection of IPs, including:
* Number of listed IPs
* Total number of blocked requests from listed IPs
* Number of IPs active in last 24 hours
* Number of stale IPs (added over 24h ago and not seen since)
* Five IPs with highest block count
* Five IPs most recently blocked
* Longest running entry
* IP counts by reason

## Utility methods
The `utils` module defines two convenience functions for updating the list from your application code:
* `add_to_blocklist(ips: set, reason="")` adds IPs to the blocklist
* `remove_from_blocklist(ip: str)` removes an entry, returning `True` if successful