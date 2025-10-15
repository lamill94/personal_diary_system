from lib.e_extractor import *

# Given an empty string
# Returns an empty string

def test_given_an_empty_string_returns_empty():
    result = e_extractor("")
    assert result == ""

# Given a string without any 'e's in it
# Returns the same string it was given

def test_given_no_es_return_same():
    result = e_extractor("cat")
    assert result == "cat"

# Given a string with one 'e' in it
# Returns the string with that e relocated to start

def test_given_one_e_returns_string_with_e_at_start():
    result = e_extractor("hello")
    assert result == "ehllo"

# Given a string with multiple 'e's in it
# Returns the string with those 'e's relocated to start

def test_given_multiple_es_returns_string_with_es_at_start():
    result = e_extractor("heleleoe")
    assert result == "eeeehllo"

# Given a string with 'e's already at the start
# It returns the same string

def test_given_multiple_es_at_start_returns_same_string():
    result = e_extractor("eeeehllo")
    assert result == "eeeehllo"