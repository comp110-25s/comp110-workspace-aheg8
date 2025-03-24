import pytest

from exercises.ex03.dictionary import invert

from exercises.ex03.dictionary import favorite_color

from exercises.ex03.dictionary import count

from exercises.ex03.dictionary import bin_len


__author__ = "730821126"


# edge case
def test_invert1():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


# use case
def test_invert2():
    my_dictionary = invert({"a": "z", "b": "y", "c": "x"})
    assert my_dictionary == ({"z": "a", "y": "b", "x": "c"})


# use case
def test_invert3():
    my_dictionary = invert({"apple": "banana"})
    assert my_dictionary == ({"banana": "apple"})


# use case
def test_count1():
    my_dictionary = count(["apple", "orange", "banana", "apple", "orange"])
    assert my_dictionary == ({"apple": 2, "orange": 2, "banana": 1})


# use case
def test_count2():
    my_dictionary = count(["pop", "pop", "pop", "pop"])
    assert my_dictionary == ({"pop": 4})


# edge case
def test_count3():
    assert count([]) == {}


# use case
def test_favorite_color1():
    my_dictionary = favorite_color({"Ryan": "blue", "Greg": "red", "Fred": "red"})
    assert my_dictionary == "red"


# use case
def test_favorite_color2():
    my_dictionary = favorite_color({"Bob": "blue", "Rob": "blue", "Bryan": "yellow"})
    assert my_dictionary == "blue"


# edge case
def test_favorite_color3():
    assert favorite_color({}) == ""


# use case
def test_bin_len1():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


# use case
def test_bin_len2():
    assert bin_len(["hey", "batter", "batter"]) == {3: {"hey"}, 6: {"batter"}}
    assert bin_len(["hi", "hello"]) == {2: {"hi"}, 5: {"hello"}}


# edge case
def test_bin_len3():
    assert bin_len([]) == {}
