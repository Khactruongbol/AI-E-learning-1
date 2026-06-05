# Phần Khắc Trường - Ràng Buộc Phức Tạp Và Điều Phối

## Vai trò chính

Khắc Trường phụ trách các ràng buộc có liên quan đến vị trí tương đối giữa các ngôi nhà và ràng buộc All-Different. Đây là phần giúp bài toán không chỉ so sánh hai thuộc tính trong cùng một nhà, mà còn biểu diễn quan hệ "bên phải" và "kế bên".

Ngoài phần code, Khắc Trường cũng là người điều phối ghép code giữa các nhóm: dữ liệu cơ bản, AC-3, Backtracking và phần tổng hợp báo cáo.

## Các dòng code cần tập trung

Trong `src/einstein_csp.py`, phần quan trọng nhất của Khắc Trường nằm ở:

- Dòng 31-37: chia 25 biến thành 5 nhóm thuộc tính để áp dụng All-Different.
- Dòng 92-99: hai hàm nền cho ràng buộc tương đối: `immediate_right` và `next_to`.
- Dòng 102-117: sinh ràng buộc All-Different cho từng nhóm.
- Dòng 120-154: khai báo 5 clue tương đối: clue 5, 10, 11, 14, 15.
- Dòng 186-187: ghép phần ràng buộc tương đối và All-Different vào bài toán chung.
- Dòng 191-223: AC-3 dùng các ràng buộc nhị phân này để cắt domain.

## Ràng buộc tương đối

Trong mô hình CSP này, mỗi thuộc tính được biểu diễn bằng vị trí nhà từ 1 đến 5. Nhờ vậy, các clue tương đối có thể viết thành công thức số học.

Các clue Khắc Trường cần xử lý:

- Clue 5: `Green = Ivory + 1`
  - Nhà xanh lá nằm ngay bên phải nhà màu ngà.
- Clue 10: `abs(Chesterfields - Fox) = 1`
  - Người hút Chesterfields ở cạnh nhà người nuôi cáo.
- Clue 11: `abs(Kools - Horse) = 1`
  - Nhà hút Kools ở cạnh nhà nuôi ngựa.
- Clue 14: `abs(Norwegian - Blue) = 1`
  - Người Na Uy sống cạnh nhà màu xanh lam.
- Clue 15: `abs(Chesterfields - Water) = 1`
  - Người hút Chesterfields có hàng xóm uống nước.

Trong code, các ràng buộc này nằm ở hàm `build_relative_constraints()` trong `src/einstein_csp.py`.

## All-Different

All-Different đảm bảo các giá trị trong cùng một nhóm thuộc tính không được trùng vị trí. Ví dụ, 5 màu nhà phải nằm ở 5 vị trí khác nhau:

```text
Red != Green != Ivory != Yellow != Blue
```

Tương tự, chương trình áp dụng All-Different cho:

- `Color`
- `Nationality`
- `Drink`
- `Tobacco`
- `Pet`

Trong code, All-Different được chuyển thành các ràng buộc nhị phân từng cặp để AC-3 có thể xử lý.

## Phần điều phối merge code

Khi các nhóm hoàn thiện phần riêng, Khắc Trường nên kiểm tra trước khi merge:

- Tất cả nhóm dùng cùng một tên biến: `OrangeJuice`, `OldGold`, `LuckyStrike`, `Chesterfields`, `Parliaments`.
- Không nhóm nào tự đổi miền vị trí nhà khỏi `{1, 2, 3, 4, 5}`.
- AC-3 nhận được danh sách binary arcs từ cùng mô hình CSP.
- Backtracking gọi lại `csp.is_consistent(...)` sau mỗi lần gán.
- Kết quả cuối cùng vẫn là `Japanese` nuôi `Zebra` và `Norwegian` uống `Water`.

## Nội dung đưa vào báo cáo

Có thể tóm tắt phần của Khắc Trường như sau:

> Để xử lý các clue tương đối, nhóm biểu diễn mỗi thuộc tính bằng vị trí ngôi nhà. Cách này biến các quan hệ "ngay bên phải" và "kế bên" thành các ràng buộc số học như `Green = Ivory + 1` hoặc `abs(A - B) = 1`. Ngoài ra, ràng buộc All-Different được áp dụng cho từng nhóm thuộc tính để đảm bảo không có hai nhà trùng màu, quốc tịch, đồ uống, thuốc lá hoặc thú cưng.
