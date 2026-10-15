import pytest
from src.greet import greet

def test_greet_basic():
    """Test with a standard name."""
    assert greet("Alice") == "Hello Alice!"

def test_greet_empty_string():
    """Test with an empty string, expecting a default greeting."""
    assert greet("") == "Hello World!"

def test_greet_none():
    """Test with None, expecting a default greeting."""
    assert greet(None) == "Hello World!"

def test_greet_with_spaces():
    """Test with a name containing spaces."""
    assert greet("John Doe") == "Hello John Doe!"

def test_greet_with_special_characters():
    """Test with a name containing special characters."""
    assert greet("C@rol-!ne") == "Hello C@rol-!ne!"

def test_greet_with_numbers():
    """Test with a name containing numbers."""
    assert greet("Agent 007") == "Hello Agent 007!"

def test_greet_unicode_characters():
    """Test with Unicode characters."""
    assert greet("こんにちは") == "Hello こんにちは!"
