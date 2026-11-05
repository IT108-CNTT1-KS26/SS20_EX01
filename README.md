# BÁO CÁO PHÂN TÍCH BẢO MẬT: XỬ LÝ CẢNH BÁO ĐĂNG NHẬP GIẢ MẠO GITHUB

## 1. Phân tích ký tự lạ & Cơ chế tấn công Homograph (IDN Homograph Attack)
- URL giả mạo: `https://githúb.com/login`
- Ký tự bất thường: Chữ `ú` (Latin Small Letter U with Acute – Unicode U+00FA) thay vì `u` chuẩn.
- Cơ chế Punycode: Tên miền thực chất ở tầng DNS là `xn--githb-7ua.com`. Kẻ tấn công lợi dụng việc hiển thị chuỗi Unicode tương đồng về thị giác để đánh lừa người dùng.

## 2. Quy trình kiểm tra an toàn trước khi nhập Master Password
1. Kiểm tra kỹ domain trên thanh địa chỉ, copy ra text thuần để xem có xuất hiện tiền tố `xn--` không.
2. Sử dụng Password Manager (Bitwarden, 1Password): Trình quản lý mật khẩu sẽ không bao giờ gợi ý tự động điền (Auto-fill) trên các domain giả mạo.
3. Kiểm tra chứng chỉ SSL/TLS và bật Passkey/FIDO2 WebAuthn (miễn nhiễm với Phishing).