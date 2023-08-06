from .standalone import reduce, map, filter, _builtin_map, _builtin_filter, each


class Pipeline:
    """
    This class allows to compose operations on a value.
    """

    _auto_transform = {
        _builtin_map: map,
        _builtin_filter: filter,
    }

    def __init__(self, start) -> None:
        self._current = start

    def then(self, fun, *args, **kwargs) -> 'Pipeline':
        """
        This method will apply the function fun to the current value
        held by the Pipeline object.

        it expects that fun's first parameter is an input. Any other
        parameter for fun will be passed in args

        As an exception for the sake of ease of use, built-ins "map" and "filter" are mapped
        to this library's version, reversing their parameters.

        :param fun: the function to apply to the current value held by the Pipeline object
        :param args: all other arguments of the `fun` function.
        :return: the updated pipeline object itself.
        """
        fun = self._auto_transform.get(fun, fun)
        self._current = fun(self._current, *args, **kwargs)
        return self

    def map(self, fun) -> 'Pipeline':
        """
        Shortcut to then(map, fun)

        Bear in mind that i builds a map object just like built-in map. add then(list) to get the list of mapped items.

        :param fun: the function used by map. Must be of type fun(x: Any) -> Any
        :return: the updated pipeline object itself.
        """
        return self.then(map, fun)

    def filter(self, fun) -> 'Pipeline':
        """
        Shortcut to then(filter, fun)

        Bear in mind that i builds a filter object just like built-in filter. add then(list) to get the list of filtered
        items.

        :param fun: the function used by filter. Must be of type fun(x: Any) -> Bool
        :return: the updated pipeline object itself.
        """
        return self.then(filter, fun)

    def reduce(self, acc, fun) -> 'Pipeline':
        """
        Shortcut to then(reduce, acc, fun)

        :param acc: the starting accumulator
        :param fun: the function used by reduce. Must be of type fun(x: Any, acc: Any) -> Any, where the return is the new acc value.
        :return: the updated pipeline object itself.
        """
        return self.then(reduce, acc, fun)

    def each(self, fun) -> 'Pipeline':
        """
        shortcut to then(each, fun)

        Will not update the current value held by the Pipeline object, just applies fun over each element of it.

        :param fun: the function used by each. Must be of type fun(x: Any). Any return value will be ignored.
        :return: the updated pipeline object itself.
        """
        return self.then(each, fun)

    def get(self):
        """
        Returns the current value held by the Pipeline object.
        """
        return self._current
