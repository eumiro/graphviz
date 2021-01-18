# tools.py - generic helpers

import os

__all__ = ['attach', 'mapping_items']


def attach(object, name):
    """Return a decorator doing ``setattr(object, name)`` with its argument.

    >>> spam = type('Spam', (object,), {})()
    >>> @attach(spam, 'eggs')
    ... def func():
    ...     pass
    >>> spam.eggs  # doctest: +ELLIPSIS
    <function func at 0x...>
    """
    def decorator(func):
        setattr(object, name, func)
        return func
    return decorator


def mapping_items(mapping):
    """Return an iterator over the ``mapping`` items, sort if it's a plain dict.

    >>> list(mapping_items({'spam': 0, 'ham': 1, 'eggs': 2}))
    [('eggs', 2), ('ham', 1), ('spam', 0)]

    >>> from collections import OrderedDict
    >>> list(mapping_items(OrderedDict(enumerate(['spam', 'ham', 'eggs']))))
    [(0, 'spam'), (1, 'ham'), (2, 'eggs')]
    """
    result = iter(mapping.items())
    if type(mapping) is dict:
        result = iter(sorted(result))
    return result
