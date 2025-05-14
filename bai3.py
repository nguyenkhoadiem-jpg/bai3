print("Bài 1: In các số chẵn từ 0 đến 10")
for i in range(0, 11):
    if i % 2 == 0:
        print(i, end=' ')
print("\n" + "-"*40)

print("Bài 2: Tìm số lớn nhất trong danh sách")
numbers = [3, 15, 8, 23, 7, 9]
max_number = numbers[0]

for num in numbers[1:]:
    if num > max_number:
        max_number = num

print("Danh sách:", numbers)
print("Số lớn nhất là:", max_number)
print("-"*40)

print("Bài 3: Quản lý sinh viên")

class SinhVien:
    def __init__(self, ma_sv, ten, diem):
        self.ma_sv = ma_sv
        self.ten = ten
        self.diem = diem

    def __str__(self):
        return f"{self.ma_sv} - {self.ten} - {self.diem}"


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them_sinh_vien(self, sv):
        self.danh_sach.append(sv)

    def hien_thi(self):
        print("Danh sách sinh viên:")
        for sv in self.danh_sach:
            print(sv)

    def tim_kiem(self, ma_sv):
        for sv in self.danh_sach:
            if sv.ma_sv == ma_sv:
                print("Tìm thấy:", sv)
                return
        print("Không tìm thấy sinh viên")

    def sap_xep_theo_diem(self):
        self.danh_sach.sort(key=lambda sv: sv.diem, reverse=True)

    def xoa_sinh_vien(self, ma_sv):
        for sv in self.danh_sach:
            if sv.ma_sv == ma_sv:
                self.danh_sach.remove(sv)
                print("Đã xóa sinh viên:", ma_sv)
                return
        print("Không tìm thấy sinh viên để xóa")


qlsv = QuanLySinhVien()
qlsv.them_sinh_vien(SinhVien("SV001", "An", 8.5))
qlsv.them_sinh_vien(SinhVien("SV002", "Bình", 7.0))
qlsv.them_sinh_vien(SinhVien("SV003", "Chi", 9.2))

qlsv.hien_thi()

print("\nTìm sinh viên có mã SV002:")
qlsv.tim_kiem("SV002")

print("\nDanh sách sau khi sắp xếp theo điểm:")
qlsv.sap_xep_theo_diem()
qlsv.hien_thi()

print("\nXóa sinh viên SV001:")
qlsv.xoa_sinh_vien("SV001")
qlsv.hien_thi()
