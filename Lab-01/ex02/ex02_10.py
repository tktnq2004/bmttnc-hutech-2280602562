def dao_nguoc_chuoi(s):
    return s[::-1]

input_str = input("Nhập một chuỗi cần đảo ngược: ")
print("Chuỗi sau khi đảo ngược:", dao_nguoc_chuoi(input_str))