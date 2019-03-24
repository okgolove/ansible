import json
import pytest
from ansible.module_utils import basic
from ansible.module_utils._text import to_bytes
import ansible.modules.web_infrastructure.sentry_project as sentry_project


def set_module_args(args):
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


def test_main_function():
    set_module_args({
        'api_token': '1234567890abcdwxyz',
        'organization': 'example',
        'project_name': 'backend',
        'project_slug': 'backend',
        'state': 'present',
        'team': 'senior',
        'url': 'localhost'
    })
    sentry_project.main()
