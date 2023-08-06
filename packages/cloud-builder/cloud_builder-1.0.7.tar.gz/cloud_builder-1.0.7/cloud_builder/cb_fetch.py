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
"""
usage: cb-fetch -h | --help
       cb-fetch --project=<github_project>
           [--branch=<name>]
           [--update-interval=<time_sec>]
           [--single-shot]

options:
    --project=<github_project>
        git clone source URI to fetch project with
        packages managed to build in cloud builder

    --branch=<name>
        git branch name

    --update-interval=<time_sec>
        Optional update interval for the project
        Default is 30sec

    --single-shot
        Optional single shot run. Only clone the repo
"""
import os
from docopt import docopt
from cloud_builder.utils.git import CBGit
from cloud_builder.version import __version__
from cloud_builder.cloud_logger import CBCloudLogger
from cloud_builder.identity import CBIdentity
from cloud_builder.exceptions import exception_handler
from cloud_builder.defaults import Defaults
from cloud_builder.project_metadata.project_metadata import CBProjectMetaData
from cloud_builder.build_request.build_request import CBBuildRequest
from cloud_builder.broker import CBMessageBroker
from cloud_builder.response.response import CBResponse
from apscheduler.schedulers.background import BlockingScheduler
from kiwi.privileges import Privileges
from typing import (
    Dict, List, Any
)


@exception_handler
def main() -> None:
    """
    cb-fetch - fetches a git repository and manages content
    changes on a configurable schedule. In case of a change
    a rebuild request is send to the message broker

    The tree structure in the git repository has to respect
    a predefined layout like in the following example:

    projects
    ├── ...
    ├── PROJECT_A
    │   └── SUB_PROJECT
    │       └── ...
    └── PROJECT_B
        ├── PACKAGE
        │   ├── .cb
        │   │    ├── cloud_builder.yml
        │   │    └── build_root.kiwi
        │   ├── PACKAGE.changes
        │   ├── PACKAGE.spec
        │   └── PACKAGE.tar.xz
        │ 
        └── IMAGE
            ├── .cb
            │    └── cloud_builder.yml
            └── IMAGE.kiwi
    """
    args = docopt(
        __doc__,
        version='CB (fetch) version ' + __version__,
        options_first=True
    )

    Privileges.check_for_root_permissions()

    log = CBCloudLogger('CBFetch', '(system)')
    log.set_logfile()

    git = CBGit(
        args['--project'], Defaults.get_runner_project_dir()
    )
    git.clone(args['--branch'] or '')

    if not args['--single-shot']:
        update_project(git, log)

        project_scheduler = BlockingScheduler()
        project_scheduler.add_job(
            lambda: update_project(git, log),
            'interval', seconds=int(args['--update-interval'] or 30)
        )
        project_scheduler.start()


def update_project(git: CBGit, log: CBCloudLogger) -> None:
    """
    Callback method registered with the BlockingScheduler
    """
    git.fetch()
    changed_projects: Dict[str, List[str]] = {}
    for changed_file in git.get_changed_files():
        if changed_file.startswith('projects'):
            package_dir = os.path.dirname(changed_file)
            if package_dir in changed_projects:
                changed_projects[package_dir].append(
                    os.path.basename(changed_file)
                )
            else:
                changed_projects[package_dir] = [
                    os.path.basename(changed_file)
                ]
    git.pull()
    broker = CBMessageBroker.new(
        'kafka', config_file=Defaults.get_broker_config()
    )
    for project_source_path in sorted(changed_projects.keys()):
        log.set_id(os.path.basename(project_source_path))
        project_config = CBProjectMetaData.get_project_config(
            os.path.join(
                Defaults.get_runner_project_dir(), project_source_path
            ), log, CBIdentity.get_request_id()
        )
        if project_config:
            if 'distributions' in project_config:
                send_package_update_request(
                    project_config, changed_projects,
                    project_source_path, broker, log
                )
            elif 'images' in project_config:
                send_image_update_request(
                    project_config, changed_projects,
                    project_source_path, broker, log
                )


def send_image_update_request(
    project_config: Dict, changed_projects: Dict, project_source_path: str,
    broker: Any, log: CBCloudLogger
) -> None:
    status_flags = Defaults.get_status_flags()
    request_action = status_flags.image_source_rebuild
    for target in project_config.get('images') or []:
        image_request = CBBuildRequest()
        image_request.set_image_build_request(
            project_source_path, target['arch'], target['selection']['name'],
            target['runner_group'], request_action
        )
        broker.send_build_request(image_request)
        request = image_request.get_data()
        response = CBResponse(
            request['request_id'], log.get_id()
        )
        response.set_image_update_request_response(
            message='Image update request scheduled',
            response_code=request_action,
            image=request['project'],
            arch=request['image']['arch'],
            selection=request['image']['selection']
        )
        log.response(response, broker)


def send_package_update_request(
    project_config: Dict, changed_projects: Dict, project_source_path: str,
    broker: Any, log: CBCloudLogger
) -> None:
    status_flags = Defaults.get_status_flags()
    request_action = status_flags.package_source_rebuild
    for target in project_config.get('distributions') or []:
        package_request = CBBuildRequest()
        package_request.set_package_build_request(
            project_source_path, target['arch'], target['dist'],
            target['runner_group'], request_action
        )
        broker.send_build_request(package_request)
        request = package_request.get_data()
        response = CBResponse(
            request['request_id'], log.get_id()
        )
        response.set_package_update_request_response(
            message='Package update request scheduled',
            response_code=request_action,
            package=request['project'],
            arch=request['package']['arch'],
            dist=request['package']['dist']
        )
        log.response(response, broker)
