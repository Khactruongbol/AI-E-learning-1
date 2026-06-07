# Phần Khắc Trường - Ràng buộc tương đối và All-Different

Đây là một phần nhỏ trong báo cáo nhóm của bài 3.3 Einstein's Riddle. Nội dung tập trung vào cách biểu diễn các ràng buộc phức tạp của bài toán CSP, không tách thành báo cáo cá nhân riêng.

## Nhiệm vụ

- Xử lý các ràng buộc tương đối giữa vị trí các ngôi nhà.
- Trình bày ràng buộc All-Different cho từng nhóm thuộc tính.
- Đảm bảo các ràng buộc này phù hợp với mô hình CSP chung của cả nhóm.

## Biểu diễn

Đánh số 5 ngôi nhà từ trái sang phải là `1, 2, 3, 4, 5`. Mỗi thuộc tính được xem như một biến nhận giá trị là vị trí ngôi nhà.

Ví dụ:

- `Norwegian = 1`: người Na Uy ở nhà số 1.
- `Milk = 3`: sữa được uống ở nhà số 3.
- `Green = Ivory + 1`: nhà xanh lá ở ngay bên phải nhà màu ngà.

## Ràng buộc tương đối

Các clue tương đối được viết dưới dạng quan hệ vị trí:

| Clue | Công thức | Ý nghĩa |
|---|---|---|
| 5 | `Green = Ivory + 1` | Nhà xanh lá nằm ngay bên phải nhà màu ngà. |
| 10 | `|Chesterfields - Fox| = 1` | Người hút Chesterfields ở cạnh nhà nuôi cáo. |
| 11 | `|Kools - Horse| = 1` | Nhà hút Kools ở cạnh nhà nuôi ngựa. |
| 14 | `|Norwegian - Blue| = 1` | Người Na Uy sống cạnh nhà xanh lam. |
| 15 | `|Chesterfields - Water| = 1` | Người hút Chesterfields có hàng xóm uống nước. |

## Ràng buộc All-Different

Trong mỗi nhóm thuộc tính, các giá trị không được trùng vị trí:

- `All-Different(Red, Green, Ivory, Yellow, Blue)`
- `All-Different(Brit, Spaniard, Ukrainian, Norwegian, Japanese)`
- `All-Different(Coffee, Tea, Milk, OrangeJuice, Water)`
- `All-Different(OldGold, Kools, Chesterfields, LuckyStrike, Parliaments)`
- `All-Different(Dog, Snails, Fox, Horse, Zebra)`

Ràng buộc này đảm bảo mỗi màu nhà, mỗi quốc tịch, mỗi đồ uống, mỗi loại thuốc lá và mỗi thú cưng chỉ xuất hiện một lần.

## Kết quả liên quan

Khi kết hợp các ràng buộc tương đối, All-Different và các clue còn lại, nghiệm cuối thỏa mãn bài toán là:

- Người nuôi Zebra: `Japanese`
- Người uống Water: `Norwegian`
