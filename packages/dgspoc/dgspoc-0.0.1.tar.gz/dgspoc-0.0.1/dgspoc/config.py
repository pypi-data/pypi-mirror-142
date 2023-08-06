"""Module containing the attributes for describe-get-system proof of concept module."""

from os import path
from textwrap import dedent

import templateapp
import regexapp
import dlapp

__version__ = '0.0.1'
version = __version__

__all__ = [
    'version',
    'Data'
]


class Data:

    # main app
    main_app_text = 'DGSPOC {}'.format(version)

    # company
    company = 'Geeks Trident LLC'
    company_url = 'https://www.geekstrident.com/'

    # URL
    repo_url = 'https://github.com/Geeks-Trident-LLC/dgspoc'
    # TODO: Need to update wiki page for documentation_url instead of README.md.
    documentation_url = path.join(repo_url, 'blob/develop/README.md')
    license_url = path.join(repo_url, 'blob/develop/LICENSE')

    # License
    years = '2022-2040'
    license_name = 'BSD 3-Clause License'
    copyright_text = 'Copyright @ {}'.format(years)
    license = dedent(
        """
        BSD 3-Clause License

        Copyright (c) {}, {}
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        1. Redistributions of source code must retain the above copyright notice, this
           list of conditions and the following disclaimer.

        2. Redistributions in binary form must reproduce the above copyright notice,
           this list of conditions and the following disclaimer in the documentation
           and/or other materials provided with the distribution.

        3. Neither the name of the copyright holder nor the names of its
           contributors may be used to endorse or promote products derived from
           this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
        AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
        IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
        FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
        DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
        SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
        CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
        OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        """.format(years, company)
    ).strip()

    @classmethod
    def get_dependency(cls):
        obj = dict(
            templateapp=dict(
                package='templateapp v{}'.format(templateapp.version),
                url='https://pypi.org/project/templateapp/'
            )
        )
        obj.update(templateapp.config.Data.get_dependency())
        obj.update(regexapp.config.Data.get_dependency())
        obj.update(dlapp.config.Data.get_dependency())
        dependencies = dict(sorted(obj.items(), key=lambda x: str(x[0])))
        return dependencies
