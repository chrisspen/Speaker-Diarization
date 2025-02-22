# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup script for the package."""

import os
import setuptools

VERSION = '0.0.6'

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package or package.startswith('#'):
                continue
            lst.append(package.strip())
    return lst

with open('README.md', 'r') as file_object:
    LONG_DESCRIPTION = file_object.read()

setuptools.setup(
    name='uisrnn-mega',
    version=VERSION,
    author='Quan Wang',
    author_email='quanw@google.com',
    description='Unbounded Interleaved-State Recurrent Neural Network',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/google/uis-rnn',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
    install_requires=get_reqs('requirements.txt')
)
