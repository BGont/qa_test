import pytest


@pytest.fixture(params=[(1, 2, 3, 4), ('a', 'b', 'c', 'd')])
def fixture_test_data(request):

    return list(request.param)


def test_append():
    t_list = [1, 2, 3]
    append_value = 4
    t_list.append(append_value)

    assert [1, 2, 3, 4] == t_list


def test_clear(fixture_test_data):
    fixture_test_data.clear()

    assert len(fixture_test_data) == 0


def test_reverse(fixture_test_data):
    reversed_test_list = fixture_test_data[::-1]
    fixture_test_data.reverse()

    assert fixture_test_data == reversed_test_list


def test_copy(fixture_test_data):
    test_list_copy = fixture_test_data.copy()
    assert fixture_test_data == test_list_copy and fixture_test_data is not test_list_copy


def test_count(fixture_test_data):
    test_value = 1
    counter = 0
    for item in fixture_test_data:
        if item == test_value:
            counter += 1

    assert counter == fixture_test_data.count(test_value)
