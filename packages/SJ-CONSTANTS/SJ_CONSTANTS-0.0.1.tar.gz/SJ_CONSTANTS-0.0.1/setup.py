#  Copyright (c) 2020  Thiago Lopes da Silva
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import find_packages, setup
import pathlib
import pkg_resources
import os
from os.path import dirname, abspath
from pathlib import Path

#from version import __version__
__version__ = "0.0.1"



def load_long_description():
    project_path = os.path.dirname(os.getcwd())
    current_directory = Path(project_path).parent
    readme_name = 'README.rst'

    with open(os.path.join(current_directory, readme_name), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name='SJ_CONSTANTS',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='https://github.com/BertVanAcker/SJ-CONSTANTS/blob/main/LICENSE',
    platforms='any',
    author='Bert Van Acker(B.MKR)',
    author_email='bva.bmkr@gmail.com',
    description='This repository contains the cross-repository constants',
    #long_description=__long_description,
    url='https://github.com/BertVanAcker/SJ-CONSTANTS',
    download_url='https://github.com/BertVanAcker/SJ-CONSTANTS',
    python_requires='>=3.5'
)
