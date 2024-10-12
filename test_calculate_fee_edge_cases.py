import pytest
from calculate_fee import calculate_shipping_fee

test_data = [
    (0.00, 20.0, "Phí thấp"),
    (50.00, 20.0, "Phí cao"),
    (0.01, 20.0, "Phí thấp"),
    (49.99, 20.0, "Phí cao"),
    (-0.01, 20.0, "Đầu vào không hợp lệ"),
    (50.01, 20.0, "Đầu vào không hợp lệ"),
    (25.00, 0.1, "Phí trung bình"),
    (25.00, 40.0, "Phí cao"),
    (25.00, 39.9, "Phí cao"),
    (25.00, -0.1, "Đầu vào không hợp lệ"),
    (25.00, 40.1, "Đầu vào không hợp lệ"),
]

@pytest.mark.parametrize("weight, distance, expected", test_data)
def test_calculate_shipping_fee(weight, distance, expected):
    assert calculate_shipping_fee(weight, distance) == expected