from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("----- Quản Lý Sinh Viên -----")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    
    choice = input("Chọn một tùy chọn (0-7): ")
    
    if choice == '1':
        print("\n1.Thêm Sinh viên")
        qlsv.nhapSinhVien()
        print("\nĐã thêm sinh viên thành công.")
    elif choice == '2':
        if qlsv.soLuongSinhVien() > 0:
            print("\n2.Cập nhật Sinh viên")
            id = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(id)
        else:
            print("Danh sách sinh viên đang trống.")
    elif choice == '3':
        if qlsv.soLuongSinhVien() > 0:
            print("\n3.Xóa Sinh viên")
            id = int(input("Nhập ID sinh viên cần xóa: "))
            sv = qlsv.findByID(id)
            if (sv != None):
                qlsv.listSinhVien.remove(sv)
                print("Đã xóa sinh viên với ID =", id)
            else:
                print("Không tìm thấy sinh viên với ID =", id)
    elif choice == '4':
        if qlsv.soLuongSinhVien() > 0:
            print("\n4.Tìm kiếm Sinh viên theo tên")
            name = input("\nNhập tên hoặc từ khóa cần tìm: ")
            listSV = qlsv.findByName(name)
            qlsv.showSinhVien(listSV)
        else:
            print("Danh sách sinh viên đang trống.")
    elif choice == '5':
        if qlsv.soLuongSinhVien() > 0:
            print("\n5.Sắp xếp sinh viên theo điểm trung bình (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên đang trống.")
    elif choice == '6':
        if qlsv.soLuongSinhVien() > 0:
            print("\n6.Sắp xếp sinh viên theo tên chuyên ngành")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên đang trống.")
    elif choice == '7':
        if qlsv.soLuongSinhVien() > 0:
            print("\n7.Danh sách Sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên đang trống.")
    elif choice == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")      