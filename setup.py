#!/usr/bin/env python

# This file is part of fteproxy.
#
# fteproxy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fteproxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fteproxy.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
from distutils.core import Extension

import os
if os.name == 'nt':
    import py2exe

with open('fte/VERSION') as fh:
    FTEPROXY_RELEASE = fh.read().strip()

if os.name == 'nt': # windows
    extra_compile_args = ['-O3',
                          # '-fstack-protector-all', # failes on mingw32
                          '-fPIE',
                          ]
elif os.uname()[0] == 'Darwin': # OSX
    extra_compile_args = ['-O3',
                          '-fstack-protector-all',
                          '-fPIE',
                          ]
else: # Linux
    extra_compile_args = ['-O3',
                          '-fstack-protector-all',
                          '-fPIE',
                          ]

fte_cDFA = Extension('fte.cDFA',
                     include_dirs=['fte',
                                   'thirdparty/re2',
                                  ],
                     library_dirs=['thirdparty/re2/obj',
                                  ],
                     extra_compile_args=extra_compile_args,
                     extra_link_args=['thirdparty/re2/obj/libre2.a',
                                      ],
                     libraries=['gmp',
                               ],
                     sources=['fte/rank_unrank.cc', 'fte/cDFA.cc'])

if os.name == 'nt': # windows
    setup(name='Format-Transforming Encrypion (FTE)',
          console=['./bin/fteproxy'],
          zipfile=None,
          options={"py2exe": {
              "optimize": 2,
              "compressed": True,
              "bundle_files": 1,
          }
          },
          version=FTEPROXY_RELEASE,
          description='FTE',
          author='Kevin P. Dyer',
          author_email='kpdyer@gmail.com',
          url='https://github.com/redjack/fte-proxy',
          ext_modules=[fte_cDFA],
          install_requires=[
               "obfsproxy",
               "pyptlib",
               "pycrypto",
               "twisted",
          ],
          )
else: # all others
    setup(name='Format-Transforming Encrypion (FTE)',
          version=FTEPROXY_RELEASE,
          description='FTE',
          author='Kevin P. Dyer',
          author_email='kpdyer@gmail.com',
          url='https://github.com/redjack/fte-proxy',
          ext_modules=[fte_cDFA],
          )
