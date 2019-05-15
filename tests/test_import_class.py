#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `import_class` package."""

import inspect

import pytest

from import_class import import_class, import_instance
from tests.import_file import ImportMe


def test_import_class():
    klass = import_class('tests.import_file.ImportMe')
    print(dir(klass))
    assert inspect.isclass(klass), 'This does not appear to be a class'
    assert not isinstance(klass, ImportMe), 'This does appear to be an ' \
        'instance'


def test_import_instance():
    instance = import_instance('tests.import_file.ImportMe')
    print(dir(instance))
    assert isinstance(instance, ImportMe), 'This does not appear to be an ' \
        'instance'
    assert not inspect.isclass(instance), 'This does appear to be a class'


def test_import_instance_with_error():
    with pytest.raises(TypeError):
        import_instance('tests.import_file.ImportMe2')
