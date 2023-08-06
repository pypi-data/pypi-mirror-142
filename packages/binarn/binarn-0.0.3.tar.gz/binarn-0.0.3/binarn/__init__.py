from typing import Any, Iterable, Tuple, Optional

__version__ = "0.0.3"
__all__ = [
    '__version__', 'find', 'find_one',
]

_none = object()
Result = Tuple[tuple, Any]


def _find(source, key, value, path=()) -> Iterable[Result]:
    if value is not _none and source == value:
        yield path, value

    if isinstance(source, dict):
        if key is not _none and key in source:
            _value = source[key]
            if value is _none or value == _value:
                yield path + (key,), source[key]

        for k, v in source.items():
            yield from _find(v, key, value, path=path + (k,))

    elif isinstance(source, (bytes, str)):
        return

    elif isinstance(source, Iterable):
        for i, item in enumerate(source):
            yield from _find(item, key, value, path + (i,))


def find(source: Any, *, key: Any = _none, value: Any = _none):
    """
    Find all usages of a key (or value).

    :param source: dictionary to search in
    :param key: key search to for
    :param value: optional value to search for
    :return:
    """
    return _find(source, key=key, value=value)


def find_one(source: Any, *, key: Any = _none, value: Any = _none) -> Optional[Result]:
    """
    Find a single key (or value) usage.

    :param source: dictionary to search in
    :param key: key search to for
    :param value: optional value to search for
    :return: a tuple of (path_to_the_key, value), or None
    """
    for res in find(source, key=key, value=value):
        return res
    return None
