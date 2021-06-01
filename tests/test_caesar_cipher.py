from caesar_cipher import __version__
import pytest
from caesar_cipher.caesar_cipher import encrypt ,decrypt,crack


def test_version():
    assert __version__ == '0.1.0'


# encrypt a string with a given shift
def test_1 ():
    actual = encrypt('abc',3)
    expected = 'def'
    assert actual == expected

# decrypt a previously encrypted string with the same shift
def test_2 ():
    actual = decrypt('def',3)
    expected = 'abc'
    assert actual == expected

# encryption should handle upper and lower case letters
def test_3 ():
    actual = encrypt('Hello World',3)
    expected = 'Hhoor Wruog'
    assert actual == expected
# encryption should allow non-alpha characters but ignore them, including white space
def test_4 ():
    actual = encrypt('Hello World *$#',3)
    expected = 'Hhoor Wruog *$#'
    assert actual == expected
# decrypt encrypted without key
def test_5 ():
    actual = 'Hello World'
    encrypted = encrypt(actual,3)
    expected  = crack(encrypted)
    assert actual == expected