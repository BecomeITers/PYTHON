# Hàm chuyển đổi từ nhị phân sang thập phân
def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

# Hàm chuyển đổi từ thập lục phân sang thập phân
def hex_to_decimal(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        return None

# Hàm chuyển đổi từ thập phân sang nhị phân
def decimal_to_binary(decimal_num):
    try:
        return bin(decimal_num)[2:]  # Loại bỏ tiền tố '0b'
    except ValueError:
        return None

# Hàm chuyển đổi từ thập phân sang thập lục phân
def decimal_to_hex(decimal_num):
    try:
        return hex(decimal_num)[2:]  # Loại bỏ tiền tố '0x'
    except ValueError:
        return None

# Hàm xử lý chuyển đổi
def convert_number(value, from_base, to_base):
    decimal_value = None
    
    # Chuyển từ hệ nhị phân hoặc thập lục phân sang thập phân
    if from_base == 2:
        decimal_value = binary_to_decimal(value)
    elif from_base == 16:
        decimal_value = hex_to_decimal(value)
    elif from_base == 10:
        decimal_value = int(value)  # Giá trị đã là thập phân
    else:
        return "Hệ thống số không được hỗ trợ!"

    # Kiểm tra nếu chuyển đổi sang thập phân thất bại
    if decimal_value is None:
        return "Giá trị nhập vào không hợp lệ!"

    # Chuyển từ thập phân sang hệ khác
    if to_base == 2:
        return decimal_to_binary(decimal_value)
    elif to_base == 16:
        return decimal_to_hex(decimal_value)
    elif to_base == 10:
        return str(decimal_value)
    else:
        return "Hệ thống số không được hỗ trợ!"

def main():
    print("Chương trình chuyển đổi hệ thống số")
    from_base = int(input("Nhập hệ thống số gốc (2, 10, 16): "))
    value = input("Nhập giá trị cần chuyển đổi: ")
    to_base = int(input("Nhập hệ thống số đích (2, 10, 16): "))
    
    result = convert_number(value, from_base, to_base)
  
    print("Kết quả:", result)

if __name__ == "__main__":
    main()
