
from gym import calculate_membership


def test_basic_membership():
    """Test the basic membership price."""
    assert calculate_membership("BASIC", [], 1) == 30
