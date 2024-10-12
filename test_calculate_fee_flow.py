import pytest
from calculate_fee import calculate_shipping_fee

def test_invalid_input():
    assert calculate_shipping_fee(-1.28, 25.8) == "Đầu vào không hợp lệ"

def test_low_fee():
    assert calculate_shipping_fee(3.78, 10.6) == "Phí thấp"

def test_high_fee_1():
    assert calculate_shipping_fee(36.20, 21.9) == "Phí cao"

def test_high_fee_2():
    assert calculate_shipping_fee(30.00, 16.9) == "Phí cao"