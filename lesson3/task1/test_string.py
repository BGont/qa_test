import pytest


@pytest.fixture(params = [('test', 6), ('test', 3)])
def zfill_fixture(request):

    return request.param


def test_zfill(zfill_fixture):
    s, pad = zfill_fixture

    zero_length = pad - len(s)

    if zero_length > 0:
        assert '0'*zero_length + s == s.zfill(pad)
    else:
        assert s.zfill(pad) == s


def test_upper():
    assert 'teststring'.upper() == 'TESTSTRING'


def test_join_with_not_strings():
    iterable = ['', 2]
    with pytest.raises(TypeError):
        ''.join(iterable)


def test_title():
    s = 'Return a verSion oF the sTRing wherE Each word is tITLECASED.'

    tiled_words = []
    words = s.split()
    for word in words:
        titled_word = word[0].upper() + word[1:].lower()
        tiled_words.append(titled_word)

    assert s.title() == ' '.join(tiled_words)


@pytest.mark.parametrize('test_string', ['hello, world', 'Hello, worlD'])
def test_islower(test_string):
    if test_string.lower() == test_string:
        assert test_string.islower()
    else:
        assert not test_string.islower()
