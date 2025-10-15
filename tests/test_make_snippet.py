from lib.make_snippet import *

# Given an empty string
# Return an empty string

def test_given_an_empty_string_return_empty_sting():
    result = make_snippet("")
    assert result == ""

# Given a string with < 5 words
# Return those words

def test_given_string_with_under_5_words_return_words():
    result = make_snippet("Hello")
    assert result == "Hello"

# Given a string with 5 words
# Return those 5 words

def test_given_string_with_5_words_return_5_words():
    result = make_snippet("Hello my name is Lauren")
    assert result == "Hello my name is Lauren"

# Given a string with > 5 words
# Return the first 5 words followed by ellipsis

def test_given_string_with_over_5_words_return_5_words_and_ellipsis():
    result = make_snippet("Hello my name is Lauren Miller")
    assert result == "Hello my name is Lauren..."