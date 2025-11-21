from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID += 1
        return maxID

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Nhập họ tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ") 
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(id, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self,ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            sv._name = input("Nhập họ tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập ngành học sinh viên: ")
            sv._diemTB = float(input("Nhập điểm trung bình sinh viên: "))
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên với ID =", ID)

    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=True)
        
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
            .format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if ( listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
                    .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
    
    