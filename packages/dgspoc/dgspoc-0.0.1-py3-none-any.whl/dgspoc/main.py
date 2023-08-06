"""Module containing the logic for describe-get-system proof of conception entry-points."""

import sys
import argparse


def show_dependency(options):
    if options.dependency:
        from platform import uname, python_version
        from dgspoc.config import Data
        lst = [
            Data.main_app_text,
            'Platform: {0.system} {0.release} - Python {1}'.format(
                uname(), python_version()
            ),
            '--------------------',
            'Dependencies:'
        ]

        for pkg in Data.get_dependency().values():
            lst.append('  + Package: {0[package]}'.format(pkg))
            lst.append('             {0[url]}'.format(pkg))

        width = max(len(item) for item in lst)
        txt = '\n'.join('| {1:{0}} |'.format(width, item) for item in lst)
        print('+-{0}-+\n{1}\n+-{0}-+'.format(width * '-', txt))
        sys.exit(0)


class Cli:
    """templateapp console CLI application."""

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='dgspoc',
            usage='%(prog)s [options]',
            description='%(prog)s module',
        )

        parser.add_argument(
            '-d', '--dependency', action='store_true',
            help='Show TemplateApp dependent package(s).'
        )

        self.parser = parser
        self.options = self.parser.parse_args()
        self.kwargs = dict()

    def validate_cli_flags(self):
        """Validate argparse `options`.

        Returns
        -------
        bool: show ``self.parser.print_help()`` and call ``sys.exit(1)`` if
        user_data flag is empty, otherwise, return True
        """

        self.parser.print_help()
        sys.exit(1)

    def run(self):
        """Take CLI arguments, parse it, and process."""
        show_dependency(self.options)
        self.validate_cli_flags()


def execute():
    """Execute template console CLI."""
    app = Cli()
    app.run()
