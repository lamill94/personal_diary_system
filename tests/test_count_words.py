from lib.count_words import *

# Given an empty string
# Returns 0 words

def test_given_empty_string_returns_0_words():
    result = count_words("")
    assert result == 0

# Given a string with one word
# Returns 1 word

def test_given_one_word_returns_1_word():
    result = count_words("Hello")
    assert result == 1

# Given a string with multiple words e.g. 5
# Returns multiples words e.g. 5

def test_given_one_word_returns_1_word():
    result = count_words("Hello my name is Lauren")
    assert result == 5