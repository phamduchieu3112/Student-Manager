📚 Chương Trình Quản Lý Sinh Viên

Chương trình Python này là một hệ thống quản lý cơ bản được thiết kế để lưu trữ, quản lý thông tin cá nhân và điểm thành phần của sinh viên. Dữ liệu được lưu trữ trực tiếp trong file mã nguồn Python, cho phép duy trì thông tin qua các lần chạy.
____________________________________________________________________________________________________________________________________________________________________

🚀 Các Chức Năng Chính

Chương trình được tổ chức thành một menu chính với hai module quản lý lớn: Lưu trữ thông tin sinh viên và Quản lí điểm các môn.
____________________________________________________________________________________________________________________________________________________________________

1. Lưu Trữ Thông Tin Sinh Viên

Chương trình này tập trung vào việc quản lý dữ liệu cá nhân của từng sinh viên.
__________________________________________________________________________________

1.1. Thêm Mới Sinh Viên (them_sinh_vien)

* Chức năng: Cho phép nhập thông tin chi tiết của một sinh viên mới vào danh sách.
* Xác thực đầu vào:
    * Mã SV: Phải là một chuỗi 8 chữ số và không được trùng với mã sinh viên đã tồn tại.
    * Họ tên: Không được chứa số và không được để trống.
    * SĐT: Phải là chuỗi 10 chữ số và bắt đầu bằng số '0' (có thể bỏ qua).
* Lưu trữ: Sau khi thêm thành công, dữ liệu mới sẽ được lưu lại trong file mã nguồn.
__________________________________________________________________________________

1.2. Xem Danh Sách Sinh Viên (hien_thi_danh_sach)

* Chức năng: Hiển thị toàn bộ thông tin cơ bản của tất cả sinh viên dưới dạng bảng rõ ràng, bao gồm: STT, Mã sinh viên, Họ và tên, Giới tính, Ngày sinh, Ngành, Khoa, Nơi sinh, và Số điện thoại.
* Thống kê: Cung cấp tổng số lượng sinh viên hiện có.
__________________________________________________________________________________

1.3. Xóa / Sửa Thông Tin Sinh Viên (xoa_sua_thong_tin)

* Truy cập: Cần nhập Mã SV để tìm và chọn sinh viên cần thao tác.
* Tùy chọn:
    * Xóa toàn bộ: Xóa vĩnh viễn sinh viên khỏi danh sách.
    * Sửa chi tiết: Cho phép cập nhật từng trường thông tin cá nhân (Họ tên, Giới tính, Ngày sinh, Ngành, Khoa, Nơi sinh, SĐT) của sinh viên đó.
* Lưu trữ: Mọi thay đổi (xóa hoặc sửa) đều được lưu lại ngay lập tức.

____________________________________________________________________________________________________________________________________________________________________

2. Quản Lý Điểm Các Môn

Module này dành riêng cho việc nhập, tính toán và xem điểm thành phần của sinh viên.
__________________________________________________________________________________

2.1. Nhập Điểm Thành Phần Các Môn (nhap_diem_thanh_phan)

* Truy cập: Cần nhập Mã SV để tìm và nhập điểm cho sinh viên.
* Điểm: Cho phép nhập điểm Chuyên cần (CC), Giữa kỳ (GK), và Cuối kỳ (CK).
* Quy tắc: Điểm phải nằm trong khoảng từ 0 đến 10.
* Lưu trữ: Điểm nhập được lưu lại trong dữ liệu sinh viên.
__________________________________________________________________________________

2.2. Xóa Điểm Thành Phần Các Môn (xoa_diem_thanh_phan)

* Chức năng: Thiết lập lại (reset) tất cả các điểm thành phần (CC, GK, CK) và Điểm tổng kết (TK) của một sinh viên về 0.0.
* Xác nhận: Yêu cầu xác nhận trước khi thực hiện xóa.
__________________________________________________________________________________

2.3. Tính và Xem Điểm Tổng Kết (tinh_diem_tong_ket)

* Tính toán: Thực hiện tính Điểm Tổng Kết (TK) cho tất cả sinh viên theo công thức:
    Điểm tổng kết = (Điểm chuyên cần * 0.1) + (Điểm giữa kì * 0.3) + (Điểm cuối kì + 0.6)
* Hiển thị: In ra một bảng điểm chi tiết, bao gồm: Điểm Chuyên cần, Điểm Giữa kỳ, Điểm Cuối kỳ, và Điểm Tổng kết đã được làm tròn một chữ số thập phân.
* Lưu trữ: Kết quả Điểm Tổng kết được cập nhật và lưu lại trong dữ liệu.
____________________________________________________________________________________________________________________________________________________________________

🛠️ Cài Đặt và Chạy Chương Trình

1. Tải file student_manager.py.
2. Chạy chương trình:
python student_manager.py
3. Lần chạy đầu tiên sẽ tạo danh sách sinh viên ban đầu (danh_sach_sinh_vien).
4. Mọi dữ liệu thay đổi (thêm, sửa, xóa, nhập điểm) sẽ được ghi lại trực tiếp vào biến danh_sach_sinh_vien trong file student_manager.py nhờ hàm luu_du_lieu_sv.

____________________________________________________________________________________________________________________________________________________________________

🧑‍💻 Credit

* Author: Phạm Đức Hiếu
* Facebook: https://www.facebook.com/share/1BoGsAyLdH/?mibextid=wwXIfr
* Instagram: https://instagram.com/pdhieuuu
* Zalo: https://zalo.me/0775907888
* Telegram: https://t.me/pdhieuuu
* X: https://x.com/pdhieuuu
* Github: https://github.com/phamduchieu3112