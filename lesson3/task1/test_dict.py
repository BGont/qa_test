import pytest


@pytest.fixture(params=[('a', 'b', 'c')])
def iterable(request):
    param = list(request.param)
    if 'test_not_hashable_type' == request.function.__name__:
        param.append({})

    return param


class TestFromKeys:

    def test_with_val(self, iterable):
        test_val = 'Success'
        test_dict = {}
        for key in iterable:
            test_dict[key] = test_val

        new_dict = dict.fromkeys(iterable, test_val)

        assert test_dict == new_dict

    def test_without_val(self, iterable):
        test_dict = {}
        for key in iterable:
            test_dict[key] = None

        new_dict = dict.fromkeys(iterable)

        assert test_dict == new_dict

    def test_with_mutable_val(self, iterable):
        test_val = []
        new_dict = dict.fromkeys(iterable, test_val)

        assert all([True if val is test_val else False for val in new_dict.values() if val is test_val])

    def test_not_hashable_type(self, iterable):
        with pytest.raises(TypeError):
            assert dict.fromkeys(iterable)


@pytest.mark.parametrize('test_dict', [{'a': 1, 'b': 2}])
def test_clear(test_dict):
    test_dict.clear()
    assert test_dict == {}
