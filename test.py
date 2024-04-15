import pytest

from reverse import reverse


s = "Hello, World!"

def test_reverse():
    assert reverse("Hello, World!") == "!dlroW ,olleH"
