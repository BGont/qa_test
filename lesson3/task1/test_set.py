from functools import partial
import pytest


class TestAdd:

    def test_add_different(self):
        t_set = {1, 2, 3}
        append_value = 4
        t_set.add(append_value)

        assert {1, 2, 3, 4} == t_set

    def test_add_existing(self):
        t_set = {1, 2, 3}
        append_value = 3
        t_set.add(append_value)

        assert {1, 2, 3} == t_set

    def test_add_not_hashable(self):
        t_set = {1, 2, 3}
        append_value = []

        with pytest.raises(TypeError):
            t_set.add(append_value)


@pytest.mark.parametrize("set_param, discard_elem", [({1, 2, 3, 4}, 2)])
def test_discard(set_param, discard_elem):
    def not_equal(arg1, arg2):
        return arg1 != arg2
    not_equal = partial(not_equal, arg2=discard_elem)

    new_set = set(filter(not_equal, set_param))

    set_param.discard(discard_elem)
    assert set_param == new_set


def test_union():
    test_set = {1, 2, 3, 4}
    addition_set = {5, 6, 7, 8}

    assert {1, 2, 3, 4, 5, 6, 7, 8} == test_set.union(addition_set)