#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE
# OVERWRITTEN WHEN PREPARING PACKAGES.
#
# IF YOU WANT TO MODIFY IT, YOU SHOULD MODIFY THE TEMPLATE
# `SETUP_TEMPLATE.py.jinja2` IN the `dev/provider_packages` DIRECTORY

"""Setup.py for the apache-airflow-providers-presto package."""

import logging
import os

from os.path import dirname
from setuptools import find_namespace_packages, setup

logger = logging.getLogger(__name__)

version = '2.1.0'

my_dir = dirname(__file__)

try:
    with open(os.path.join(my_dir, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

def do_setup():
    """Perform the package apache-airflow-providers-presto setup."""
    setup(
        name='apache-airflow-providers-presto',
        description='Provider package apache-airflow-providers-presto for Apache Airflow',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        license='Apache License 2.0',
        version=version,
        packages=find_namespace_packages(include=['airflow.providers.presto', 'airflow.providers.presto.*']),
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            'apache-airflow>=2.1.0',
            'pandas>=0.17.1, <1.4',
            'presto-python-client>=0.7.0,<0.8',
        ],
        setup_requires=['setuptools', 'wheel'],
        extras_require={'google': ['apache-airflow-providers-google']},
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: System :: Monitoring',
        ],
        author='Apache Software Foundation',
        author_email='dev@airflow.apache.org',
        url='https://airflow.apache.org/',
        download_url='https://archive.apache.org/dist/airflow/providers',
        python_requires='~=3.6',
        project_urls={
            'Documentation': 'https://airflow.apache.org/docs/apache-airflow-providers-presto/2.1.0/',
            'Bug Tracker': 'https://github.com/apache/airflow/issues',
            'Source Code': 'https://github.com/apache/airflow',
            'Slack Chat': 'https://s.apache.org/airflow-slack',
            'Twitter': 'https://twitter.com/ApacheAirflow',
            'YouTube': 'https://www.youtube.com/channel/UCSXwxpWZQ7XZ1WL3wqevChA/',
        },
    )

if __name__ == "__main__":
    do_setup()
