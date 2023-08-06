"""
Standalone functions to use for your functional needs.
"""

_builtin_map = map
_builtin_filter = filter


def reduce(iterable, acc, fun):
    """
    :param iterable: any iterable
    :param acc: the starting accumulator
    :param fun: function used for reduce, in the form of fun(iterable_item, acc) -> new_acc_value
    :return:
    """
    for x in iterable:
        acc = fun(x, acc)
    return acc


# noinspection PyShadowingBuiltins
def map(iterable, fun):
    """
    return a generator object of built-in map.

    built-in map's parameter are map(func, *iterables). This only reverses the parameter for a functional programming
    approach.

    :param iterable: any iterable.
    :param fun: the function to apply.
    :return:
    """
    return _builtin_map(fun, iterable)


def filter(iterable, fun):
    """
    returns a generator object from built-in filter.

    built-in filter's parameter are filter(func, *iterables). This only reverses the parameter for a functional
    programming approach.

    :param iterable: any iterable.
    :param fun: the filter to apply
    :return:
    """
    return _builtin_filter(fun, iterable)


def each(iterable, fun):
    """
    Applies the function "fun" to each item in iterable.

    SIDE EFFECT WARNING: If iterable was a generator, each will return a list of all items generated
    after it applied its logic.

    If iterable was a list, it returns the exact same list.

    This is sadly a side effect of not being able to copy a generator object in Python.

    :param iterable: any iterable
    :param fun: the function to apply to each item.
    :return: list(iterable)
    """
    iterable = list(iterable)
    [fun(x) for x in iterable]
    return iterable
