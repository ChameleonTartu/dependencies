# -*- coding: utf-8 -*-
import inspect

from _dependencies.exceptions import DependencyError


def _check_class(function):

    if inspect.isclass(function):
        raise DependencyError("'operation' decorator can not be used on classes")


def _check_method(arguments):

    if "self" in arguments:
        raise DependencyError("'operation' decorator can not be used on methods")
