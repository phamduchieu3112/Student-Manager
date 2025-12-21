import os

danh_sach_sinh_vien = [{'stt': 1, 'ma_sv': '25023599', 'ho_ten': 'Phạm Đức Hiếu', 'gioi_tinh': 'Nam', 'ngay_sinh': '31/12/2007', 'nganh': 'Kĩ Thuật Robot', 'khoa': 'Điện Tử Viễn Thông', 'noi_sinh': 'Hà Nội', 'sdt': '0775907888', 'diem_cc': 0.0, 'diem_gk': 0.0, 'diem_ck': 0.0, 'diem_tk': 0.0, 'xep_loai': ''}]

def luu_du_lieu_sv(ds_lop):
    du_lieu_moi = repr(ds_lop)
    ten_file = __file__
    
    f_read = open(ten_file, 'r', encoding='utf-8')
    lines = f_read.readlines()
    f_read.close()
    
    new_lines = []
    for line in lines:
        if line.startswith("danh_sach_sinh_vien ="):
            new_lines.append(f"danh_sach_sinh_vien = {du_lieu_moi}\n")
        else:
            new_lines.append(line)
            
    f_write = open(ten_file, 'w', encoding='utf-8')
    f_write.writelines(new_lines)
    f_write.close()

def xoa_man_hinh():
    print("-" * 60)

def tieu_de_menu(text):
    print("="*60)
    print(f" {text.upper()}") 
    print("="*60)

def dung_man_hinh():
    input("\n>> Nhấn Enter để tiếp tục...")

def chuan_hoa_ten(text):
    if len(text) > 0:
        return text.title()
    return ""

def tim_index_sv(ds_lop, msv):
    for i in range(len(ds_lop)):
        if ds_lop[i]['ma_sv'] == msv:
            return i
    return -1

def kiem_tra_ma_sv(msv):
    return len(msv) == 8 and msv.isdigit()

def kiem_tra_ten(ten):
    for char in ten:
        if char.isdigit():
            return False
    return True

def kiem_tra_sdt(sdt):
    return len(sdt) == 10 and sdt.isdigit() and sdt.startswith('0')

def them_sinh_vien(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("Thêm sinh viên mới")
    stt = len(ds_lop) + 1
    print(f">> Nhập thông tin cho sinh viên thứ {stt}:")

    while True:
        msv = input("   - Mã SV (8 số): ").strip()
        if msv == "": return
        
        if kiem_tra_ma_sv(msv):
            if tim_index_sv(ds_lop, msv) != -1:
                print("     [!] Lỗi: Mã SV đã tồn tại!")
            else:
                break
        else:
            print("     [!] Lỗi: Mã SV phải có 8 chữ số.")

    while True:
        ten = input("   - Họ tên: ").strip()
        if kiem_tra_ten(ten) and len(ten) > 0:
            ten = chuan_hoa_ten(ten)
            break
        print("     [!] Lỗi: Tên không được chứa số hoặc để trống.")

    gt = chuan_hoa_ten(input("   - Giới tính: "))
    ns = input("   - Ngày sinh (dd/mm/yyyy): ")
    nganh = chuan_hoa_ten(input("   - Ngành: "))
    khoa = chuan_hoa_ten(input("   - Khoa: "))
    noi_sinh = chuan_hoa_ten(input("   - Nơi sinh: "))

    while True:
        sdt = input("   - SĐT: ").strip()
        if sdt == "": break
        if kiem_tra_sdt(sdt): break
        print("     [!] Lỗi: SĐT phải 10 số, bắt đầu bằng 0.")

    sv_moi = {
        'stt': stt,
        'ma_sv': msv,
        'ho_ten': ten,
        'gioi_tinh': gt,
        'ngay_sinh': ns,
        'nganh': nganh,
        'khoa': khoa,
        'noi_sinh': noi_sinh,
        'sdt': sdt,
        'diem_cc': 0.0,
        'diem_gk': 0.0,
        'diem_ck': 0.0,
        'diem_tk': 0.0,
        'xep_loai': ''
    }
    
    ds_lop.append(sv_moi)
    luu_du_lieu_sv(ds_lop)
    
    print(f"\n[OK] Đã thêm sinh viên {ten} thành công!")
    dung_man_hinh()

def hien_thi_danh_sach(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("DANH SÁCH SINH VIÊN")
    print(f"{'STT':<5} | {'Mã sinh viên':<15} | {'Họ và tên':<25} | {'Giới tính':<10} | {'Ngày sinh':<15} | {'Ngành':<30} | {'Khoa':<31} | {'Nơi sinh':<12} | {'Số điện thoại':<15}")
    print("-" * 180)
    
    for stt, sv in enumerate(ds_lop, start=1):
        print(f"{stt:<5} | {sv['ma_sv']:<15} | {sv['ho_ten']:<25} | {sv['gioi_tinh']:<10} | {sv['ngay_sinh']:<15} | {sv['nganh']:<30} | {sv['khoa']:<31} | {sv['noi_sinh']:<12} | {sv['sdt']:<15}")
    
    print(f"\nTổng số: {len(ds_lop)} sinh viên")
    dung_man_hinh()

def xoa_sua_thong_tin(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("Xóa / Sửa thông tin")
    
    msv = input(">> Nhập Mã SV cần thao tác: ").strip()
    idx = tim_index_sv(ds_lop, msv)
    
    if idx == -1:
        print(f"\n[!] Không tìm thấy sinh viên có mã {msv}")
        dung_man_hinh()
        return
    
    sv = ds_lop[idx]
    print(f"-> Đang chọn: {sv['ho_ten']}")
    print("-" * 40)

    print("1. Xóa toàn bộ thông tin của sinh viên này")
    print("2. Sửa Họ và tên")
    print("3. Sửa Giới tính")
    print("4. Sửa Ngày sinh")
    print("5. Sửa Ngành học")
    print("6. Sửa Khoa")
    print("7. Sửa Nơi sinh")
    print("8. Sửa SĐT")
    print("0. Quay lại")
    
    chon = input("Lựa chọn: ")
    
    updated = False
    
    if chon == '1':
        xac_nhan = input("Xác nhận xóa? (y/n): ")
        if xac_nhan == 'y':
            ds_lop.pop(idx)
            print("\n[OK] Đã xóa sinh viên.")
            updated = True
    
    elif chon == '2':
        moi = input("Nhập tên mới: ")
        if len(moi) > 0: 
            sv['ho_ten'] = chuan_hoa_ten(moi)
            updated = True
        print("[OK] Đã cập nhật.")
        
    elif chon == '3':
        moi = input("Nhập Giới tính mới: ")
        sv['gioi_tinh'] = chuan_hoa_ten(moi)
        updated = True
        print("[OK] Đã cập nhật.")

    elif chon == '4':
        moi = input("Nhập Ngày sinh mới (dd/mm/yyyy): ")
        sv['ngay_sinh'] = moi
        updated = True
        print("[OK] Đã cập nhật.")
        
    elif chon == '5':
        moi = input("Nhập ngành mới: ")
        sv['nganh'] = chuan_hoa_ten(moi)
        updated = True
        print("[OK] Đã cập nhật.")
        
    elif chon == '6':
        moi = input("Nhập Khoa mới: ")
        sv['khoa'] = chuan_hoa_ten(moi)
        updated = True
        print("[OK] Đã cập nhật.")

    elif chon == '7':
        moi = input("Nhập Nơi sinh mới: ")
        sv['noi_sinh'] = chuan_hoa_ten(moi)
        updated = True
        print("[OK] Đã cập nhật.")
            
    elif chon == '8':
        moi = input("Nhập SĐT mới: ")
        if kiem_tra_sdt(moi):
            sv['sdt'] = moi
            updated = True
            print("[OK] Đã cập nhật.")
        else:
            print("[!] SĐT không hợp lệ.")
    
    if updated:
        luu_du_lieu_sv(ds_lop)
            
    if chon != '0' and chon != '1':
        dung_man_hinh()

def luu_tru_thong_tin_sinh_vien(ds_lop):
    while True:
        xoa_man_hinh()
        print("="*60)
        print(" HỆ THỐNG LƯU TRỮ THÔNG TIN SINH VIÊN")
        print("="*60)
        print("[1] Thêm mới sinh viên")
        print("[2] Xem danh sách sinh viên") 
        print("[3] Xóa/Sửa thông tin sinh viên")
        print("[4] Quay lại Menu chính")
        
        chon = input("\nLựa chọn chức năng: ")
        
        if chon == '1':
            them_sinh_vien(ds_lop)
        elif chon == '2':
            hien_thi_danh_sach(ds_lop)
        elif chon == '3':
            xoa_sua_thong_tin(ds_lop)
        elif chon == '4':
            break

def nhap_diem_thanh_phan(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("Nhập điểm thành phần")
    
    msv = input(">> Nhập Mã SV cần vào điểm: ").strip()
    idx = tim_index_sv(ds_lop, msv)
    
    if idx != -1:
        sv = ds_lop[idx]
        print(f"-> Đang nhập điểm cho: {sv['ho_ten']}")
        print("Lưu ý: Nhập số thập phân (Ví dụ 8.5)")
        cc = float(input("   - Điểm Chuyên cần (10%): "))
        gk = float(input("   - Điểm Giữa kỳ    (30%): "))
        ck = float(input("   - Điểm Cuối kỳ    (60%): "))
        
        if (0 <= cc <= 10) and (0 <= gk <= 10) and (0 <= ck <= 10):
            sv['diem_cc'] = cc
            sv['diem_gk'] = gk
            sv['diem_ck'] = ck
            luu_du_lieu_sv(ds_lop)
            print(f"\n[OK] Đã lưu điểm cho {sv['ho_ten']} thành công!")
        else:
            print("\n[!] Lỗi: Điểm phải từ 0 đến 10.")
    else:
        print(f"\n[!] Không tìm thấy sinh viên có mã {msv}")
    dung_man_hinh()

def xoa_diem_thanh_phan(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("Xóa điểm thành phần")
    msv = input(">> Nhập Mã SV cần xóa điểm: ").strip()
    idx = tim_index_sv(ds_lop, msv)
    
    if idx != -1:
        sv = ds_lop[idx]
        xac_nhan = input(f"Xác nhận xóa điểm của {sv['ho_ten']}? (y/n): ")
        if xac_nhan == 'y':
            sv['diem_cc'] = 0.0
            sv['diem_gk'] = 0.0
            sv['diem_ck'] = 0.0
            sv['diem_tk'] = 0.0
            luu_du_lieu_sv(ds_lop)
            print("\n[OK] Đã reset điểm về 0.")
    else:
        print("[!] Không tìm thấy MSV.")
    dung_man_hinh()

def tinh_diem_tong_ket(ds_lop):
    xoa_man_hinh()
    tieu_de_menu("Tính điểm tổng kết")
    print("Đang tính toán...")
    
    count = 0
    for sv in ds_lop:
        tk = (sv['diem_cc'] * 0.1) + (sv['diem_gk'] * 0.3) + (sv['diem_ck'] * 0.6)
        sv['diem_tk'] = tk
        count += 1
    
    luu_du_lieu_sv(ds_lop)
    print(f"\n[OK] Đã tính điểm xong cho {count} sinh viên.")

    print("\nBẢNG ĐIỂM CHI TIẾT:")
    print(f"{'STT':<5} | {'Mã sinh viên':<15} | {'Họ và tên':<20} | {'Chuyên cần':<15} | {'Giữa kì':<15} | {'Cuối kì':<15} | {'Điểm tổng':<15}")
    print("-" * 112)
    for stt, sv in enumerate(ds_lop, start=1):
        print(f"{stt:<5} | {sv['ma_sv']:<15} | {sv['ho_ten']:<20} | {sv['diem_cc']:<15.1f} | {sv['diem_gk']:<15.1f} | {sv['diem_ck']:<15.1f} | {sv['diem_tk']:<15.1f}")
        
    dung_man_hinh()

def quan_li_diem(ds_lop):
    while True:
        xoa_man_hinh()
        print("="*60)
        print(" HỆ THỐNG QUẢN LÝ ĐIỂM")
        print("="*60)
        print("[1] Nhập điểm thành phần các môn")
        print("[2] Xóa điểm thành phần các môn")
        print("[3] Tính và Xem điểm tổng kết")
        print("[4] Quay lại Menu chính")
        
        chon = input("\nLựa chọn chức năng: ")
        
        if chon == '1':
            nhap_diem_thanh_phan(ds_lop)
        elif chon == '2':
            xoa_diem_thanh_phan(ds_lop)
        elif chon == '3':
            tinh_diem_tong_ket(ds_lop)
        elif chon == '4':
            break

def main():
    os.system('title Chương trình quản lí SV')
    
    ds_lop = danh_sach_sinh_vien
    
    while True:
        xoa_man_hinh()
        banner = """
██╗░░░██╗███████╗████████╗  ██╗░░░██╗███╗░░██╗██╗░░░██╗
██║░░░██║██╔════╝╚══██╔══╝  ██║░░░██║████╗░██║██║░░░██║
██║░░░██║█████╗░░░░░██║░░░  ╚██╗░██╔╝██╔██╗██║██║░░░██║
██║░░░██║██╔══╝░░░░░██║░░░  ░╚████╔╝░██║╚████║██║░░░██║
╚██████╔╝███████╗░░░██║░░░  ░░╚██╔╝░░██║░╚███║╚██████╔╝
░╚═════╝░╚══════╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚══╝░╚═════╝░
▶ Chương trình quản lí sinh viên trường Đại học Công nghệ Đại học Quốc gia Hà Nội
▶ Chương trình này được tạo ra bởi sinh viên Phạm Đức Hiếu
"""
        print(banner)
        print('┌──────────────────────────────────────┐')
        print('║   Lưu trữ thông tin sinh viên        ║')
        print('└──────────────────────────────────────┘')
        print('[1] Nhập, xóa dữ liệu sinh viên')
        print('─────────────────────────────────────────────────')
        print('┌───────────────────────────────┐')
        print('║      Quản lí điểm các môn     ║')
        print('└───────────────────────────────┘')
        print('[2] Nhập, xóa, tính điểm thành phần các môn')
        print('─────────────────────────────────────────────────')
        print('┌───────────────────────────────┐')
        print('║      Tạm biệt UET-ers         ║')
        print('└───────────────────────────────┘')
        print("[3] Thoát chương trình quản lí sinh viên")
        print('─────────────────────────────────────────────────')

        choice = input('Chọn chức năng (chỉ nhập số): ')
        if choice == "1":
            luu_tru_thong_tin_sinh_vien(ds_lop)
        elif choice == "2":
            quan_li_diem(ds_lop)
        elif choice == "3":
            print("Tạm biệt UET-er!")
            input("Nhấn Enter để thoát...")
            break
        else:
            print("Vui lòng chọn đúng chức năng !!")
            input("Nhấn Enter để thử lại...")

if __name__ == "__main__":
    main()