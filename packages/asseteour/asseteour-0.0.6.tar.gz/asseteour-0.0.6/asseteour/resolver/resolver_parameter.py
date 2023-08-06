"""Populate the property objects
"""
import copy
import json
import os
import typing
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List

from compipe.exception.validate_error import GErrorNullObject, GErrorValue
from compipe.response.command_result import MSGStatusCodes
from compipe.utils.logging import logger
from compipe.utils.parameters import (ARG_DATA, ARG_FILE, ARG_GUID, ARG_NAME,
                                      ARG_OBJ, ARG_PARENT)
from compipe.utils.task_queue_helper import TQHelper
from github_app.github_helper import JsonPropertiesHelper
from pydantic import BaseModel, Field


class SchemaRepo(BaseModel):

    repo: str = Field('',
                      title='git repo name',
                      description='represent the repo full path.')

    path: str = Field('',
                      title='the repo path of the schema file',
                      description='represent the resolver name.')

    main_branch: str = Field('',
                             title='main branch name',
                             description='represent the resolver name.')


class ResolverParam(BaseModel):
    #
    filter_source: str = Field('',
                               title='Source filter (regex)',
                               description='represent the source filter pattern for looking for the matched configs')

    filter_export: str = Field('',
                               title='export filter (regex)',
                               description='represent the export fitler pattern which would be used to check if the config'
                               'is an "add" commit. The repo helper would perform "add" behavior instead of "update"')

    output_path: str = Field('',
                             title='Output path',
                             description='the target path for storing the full payload configs.')

    ignore_paths: List[str] = Field([],
                                    title='Ignore path list',
                                    description='represent the paths for excluding the configs when populating full payload data')

    repo: str = Field('',
                      title='git repo name',
                      description='represent the repo full path.')

    name: str = Field('',
                      title='resolver name',
                      description='represent the resolver name.')

    main_branch: str = Field('',
                             title='main branch name',
                             description='represent the resolver name.')

    model_name: str = Field('',
                            title='model class name',
                            description='represent the pydantic model class name.')

    model: typing.Any = Field(None,
                              title='model object',
                              description='represent the pydantic model object.')

    resolver: typing.Any = Field(None,
                                 title='resolver object',
                                 description='represent the pydantic resolver object.')

    model_schema: SchemaRepo = Field(None,
                                     title='schema git repo definition',
                                     description='Represent the git repo information which would '
                                     'be used to export the schema file.')
