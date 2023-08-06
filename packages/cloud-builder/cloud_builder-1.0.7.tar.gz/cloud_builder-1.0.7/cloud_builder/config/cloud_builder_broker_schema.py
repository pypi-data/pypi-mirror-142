# Copyright (c) 2021 Marcus Schaefer.  All rights reserved.
#
# This file is part of Cloud Builder.
#
# Cloud Builder is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cloud Builder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cloud Builder.  If not, see <http://www.gnu.org/licenses/>
#
cloud_builder_broker_schema = {
    'broker': {
        'required': True,
        'type': 'dict',
        'schema': {
            'host': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'tls': {
                'required': False,
                'type': 'dict',
                'schema': {
                    'ssl_cafile': {
                        'required': True,
                        'type': 'string',
                        'nullable': False
                    },
                    'ssl_certfile': {
                        'required': True,
                        'type': 'string',
                        'nullable': False
                    },
                    'ssl_keyfile': {
                        'required': True,
                        'type': 'string',
                        'nullable': False
                    }
                }
            }
        }
    },
    'runner': {
        'required': False,
        'type': 'dict',
        'schema': {
            'group': {
                'required': True,
                'type': 'string',
                'nullable': False
            }
        }
    },
    'this_host': {
        'required': True,
        'type': 'string',
        'nullable': False
    }
}
