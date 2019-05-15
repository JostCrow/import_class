# -*- coding: utf-8 -*-
from importlib import import_module

"""Top-level package for import_class."""

__author__ = """Jorik Kraaikamp"""
__email__ = 'jorikkraaikamp@gmail.com'
__version__ = '0.2.0'


def import_class(path):
    package, klass = path.rsplit('.', 1)
    module = import_module(package)
    return getattr(module, klass)


def import_instance(path):
    package, class_name = path.rsplit('.', 1)
    module = import_module(package)
    klass = getattr(module, class_name)
    return klass()
