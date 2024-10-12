import pytest
from calculate_fee import calculate_shipping_fee
test_data = [
    (-97.96, -20.6, "Đầu vào không hợp lệ"),
    (97.84, -90.7, "Đầu vào không hợp lệ"),
    (6.33, -2.8, "Đầu vào không hợp lệ"),
    (12.65, -79.2, "Đầu vào không hợp lệ"),
    (37.05, -4.6, "Đầu vào không hợp lệ"),
    (-56.97, 79.1, "Đầu vào không hợp lệ"),
    (59.33, 80.0, "Đầu vào không hợp lệ"),
    (5.91, 78.4, "Đầu vào không hợp lệ"),
    (16.58, 96.7, "Đầu vào không hợp lệ"),
    (49.96, 78.4, "Đầu vào không hợp lệ"),
    (-36.82, 79.1, "Đầu vào không hợp lệ"),
    (7.17, 0.5, "Phí thấp"),
    (12.74, 9.1, "Phí trung bình"),
    (36.80, 5.6, "Phí cao"),
    (-69.23, 26.9, "Đầu vào không hợp lệ"),
    (58.50, 9.0, "Đầu vào không hợp lệ"),
    (2.12, 28.2, "Phí trung bình"),
    (13.72, 26.4, "Phí trung bình"),
    (91.80, 36.2, "Đầu vào không hợp lệ"),
    (30.23, 33.9, "Phí cao"),
    (12.81, 28.2, "Phí trung bình"),
    (41.01, 21.0, "Phí cao"),
    (38.23, 32.8, "Phí cao"),
    (40.07, 36.2, "Phí cao"),
]

@pytest.mark.parametrize("weight, distance, expected", test_data)
def test_shipping_fee(weight, distance, expected):
    assert calculate_shipping_fee(weight, distance) == expected