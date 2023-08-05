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
# `get_provider_info_TEMPLATE.py.jinja2` IN the `provider_packages` DIRECTORY

def get_provider_info():
    return {
        'package-name': 'apache-airflow-providers-apache-druid',
        'name': 'Apache Druid',
        'description': '`Apache Druid <https://druid.apache.org/>`__.\n',
        'versions': [
            '2.3.1',
            '2.3.0',
            '2.2.0',
            '2.1.0',
            '2.0.2',
            '2.0.1',
            '2.0.0',
            '1.1.0',
            '1.0.1',
            '1.0.0',
        ],
        'additional-dependencies': ['apache-airflow>=2.1.0'],
        'integrations': [
            {
                'integration-name': 'Apache Druid',
                'external-doc-url': 'https://druid.apache.org/',
                'logo': '/integration-logos/apache/druid-1.png',
                'how-to-guide': ['/docs/apache-airflow-providers-apache-druid/operators.rst'],
                'tags': ['apache'],
            }
        ],
        'operators': [
            {
                'integration-name': 'Apache Druid',
                'python-modules': [
                    'airflow.providers.apache.druid.operators.druid',
                    'airflow.providers.apache.druid.operators.druid_check',
                ],
            }
        ],
        'hooks': [
            {
                'integration-name': 'Apache Druid',
                'python-modules': ['airflow.providers.apache.druid.hooks.druid'],
            }
        ],
        'hook-class-names': ['airflow.providers.apache.druid.hooks.druid.DruidDbApiHook'],
        'connection-types': [
            {
                'hook-class-name': 'airflow.providers.apache.druid.hooks.druid.DruidDbApiHook',
                'connection-type': 'druid',
            }
        ],
        'transfers': [
            {
                'source-integration-name': 'Apache Hive',
                'target-integration-name': 'Apache Druid',
                'python-module': 'airflow.providers.apache.druid.transfers.hive_to_druid',
            }
        ],
    }
