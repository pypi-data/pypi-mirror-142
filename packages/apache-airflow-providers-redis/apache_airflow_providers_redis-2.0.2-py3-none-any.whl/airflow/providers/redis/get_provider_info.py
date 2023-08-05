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
        'package-name': 'apache-airflow-providers-redis',
        'name': 'Redis',
        'description': '`Redis <https://redis.io/>`__\n',
        'versions': ['2.0.2', '2.0.1', '2.0.0', '1.0.1', '1.0.0'],
        'additional-dependencies': ['apache-airflow>=2.1.0'],
        'integrations': [
            {
                'integration-name': 'Redis',
                'external-doc-url': 'https://redis.io/',
                'logo': '/integration-logos/redis/Redis.png',
                'tags': ['software'],
            }
        ],
        'operators': [
            {
                'integration-name': 'Redis',
                'python-modules': ['airflow.providers.redis.operators.redis_publish'],
            }
        ],
        'sensors': [
            {
                'integration-name': 'Redis',
                'python-modules': [
                    'airflow.providers.redis.sensors.redis_key',
                    'airflow.providers.redis.sensors.redis_pub_sub',
                ],
            }
        ],
        'hooks': [{'integration-name': 'Redis', 'python-modules': ['airflow.providers.redis.hooks.redis']}],
        'hook-class-names': ['airflow.providers.redis.hooks.redis.RedisHook'],
        'connection-types': [
            {'hook-class-name': 'airflow.providers.redis.hooks.redis.RedisHook', 'connection-type': 'redis'}
        ],
    }
