# -*- coding: utf-8 -*-
from dependencies import operation


@operation
def Foo(bar):
    """Define operation with circle error."""
    pass  # pragma: no cover


@operation
def Bar(foo):
    """Define operation with circle error."""
    pass  # pragma: no cover
