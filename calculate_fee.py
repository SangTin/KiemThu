def calculate_shipping_fee(weight, distance):
    if not(0 <= weight <= 50) or not(0 <= distance <= 40):
        return "Đầu vào không hợp lệ"
    elif 0 <= weight <= 10 and 0 <= distance < 20:  # CORRECT: 0 <= distance <= 20
        return "Phí thấp"
    elif 30 < weight <= 50 or 30 <= distance <= 40:  # CORRECT: 30 <= weight <= 50
        return "Phí cao"
    return "Phí trung bình"