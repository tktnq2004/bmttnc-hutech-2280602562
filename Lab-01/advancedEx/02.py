import re

def tinh_tong_so(chuoi):
    nums = re.findall(r'-?\d+', chuoi)

    tong_duong = 0
    tong_am = 0

    for n in nums:
        n = int(n)
        if n >= 0:
            tong_duong += n
        else:
            tong_am += n

    return tong_duong, tong_am

s = "-100#^sdfkj8902w3ir021@swf-20"
duong, am = tinh_tong_so(s)

print("Giá trị dương:", duong)
print("Giá trị âm:", am)
