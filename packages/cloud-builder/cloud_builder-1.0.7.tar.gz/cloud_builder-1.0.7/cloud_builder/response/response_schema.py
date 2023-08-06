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
response_schema = {
    'schema_version': {
        'required': True,
        'type': 'number',
        'nullable': False
    },
    'identity': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'request_id': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'message': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'response_code': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'project': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'target': {
        'required': False,
        'type': 'dict',
        'schema': {
            'arch': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'dist': {
                'required': False,
                'type': 'string',
                'nullable': False
            },
            'selection': {
                'required': False,
                'type': 'string',
                'nullable': False
            }
        }
    },
    'package_prepare': {
        'required': False,
        'type': 'dict',
        'schema': {
            'prepare_log_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'build_root': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'solver_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'exit_code': {
                'required': True,
                'type': 'number'
            }
        }
    },
    'package': {
        'required': False,
        'type': 'dict',
        'schema': {
            'prepare_log_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'log_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'solver_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'binary_packages': {
                'required': True,
                'type': 'list',
                'nullable': False
            },
            'exit_code': {
                'required': True,
                'type': 'number'
            }
        }
    },
    'image': {
        'required': False,
        'type': 'dict',
        'schema': {
            'log_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'solver_file': {
                'required': True,
                'type': 'string',
                'nullable': False
            },
            'binary_packages': {
                'required': True,
                'type': 'list',
                'nullable': False
            },
            'exit_code': {
                'required': True,
                'type': 'number'
            }
        }
    }
}
