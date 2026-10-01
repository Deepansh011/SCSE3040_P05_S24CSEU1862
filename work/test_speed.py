"Tests for delivery speed."

import pytest

from orders import minutes_per_km


def test_slow_delivery():
    # 60 minutes for 6 km = 10 minutes per km
    assert minutes_per_km(60, 6) == 10.0


def test_negative_distance_raises():
    # Negative distance should not be allowed
    with pytest.raises(ValueError):
        minutes_per_km(30, -3)
