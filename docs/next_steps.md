# Hướng Dẫn Các Phần Kế Tiếp

## Nhóm dữ liệu, unary và binary constraints

Việc cần làm:

- Đối chiếu lại đủ 15 clue trong đề với `build_problem()`.
- Code hiện đã được rút gọn để dễ đọc, nên khi bổ sung chỉ nên thêm constraint theo mẫu `Constraint(left, right, predicate, note)`.
- Kiểm tra các clue cùng nhà:
  - `Brit == Red`
  - `Spaniard == Dog`
  - `Coffee == Green`
  - `Ukrainian == Tea`
  - `OldGold == Snails`
  - `Kools == Yellow`
  - `LuckyStrike == OrangeJuice`
  - `Japanese == Parliaments`
- Kiểm tra unary constraints:
  - `Milk == 3`
  - `Norwegian == 1`

## Nhóm AC-3

Code hiện đã có hàm `ac3(csp)`. Nếu báo cáo cần trace chi tiết, nhóm AC-3 có thể bổ sung log:

- In arc đang xét: `(Xi, Xj)`.
- In domain trước khi `Revise`.
- In giá trị bị loại khỏi domain.
- In queue sau khi thêm lại các arc liên quan.
- Không cần đổi cấu trúc dữ liệu nếu chỉ cần trace; thêm `print(...)` trong `ac3()` và `revise()` là đủ.

Gợi ý báo cáo:

```text
Revise(Xi, Xj): loại value x khỏi D(Xi) nếu không tồn tại y trong D(Xj) sao cho constraint(Xi, Xj) đúng.
```

## Nhóm Backtracking và Heuristics

Code hiện dùng MRV để chọn biến có domain nhỏ nhất trước. Nhóm Backtracking có thể bổ sung phần giải thích:

- Backtracking thử từng giá trị trong domain còn lại.
- Sau mỗi lần gán, chương trình kiểm tra consistency.
- AC-3 được gọi lại trên trạng thái mới để cắt miền sớm hơn.
- MRV giúp ưu tiên biến khó nhất trước, giảm số nhánh cần thử.

Nếu muốn mở rộng, có thể thêm Forward Checking riêng hoặc Least Constraining Value, nhưng không bắt buộc để giải đúng bài này.

## Nhóm báo cáo tổng hợp

Báo cáo nên có các phần:

- Mô tả bài toán Zebra Puzzle.
- Bảng biến, domain và constraint.
- Constraint graph ở mức nhóm thuộc tính hoặc mức biến.
- Pseudo-code AC-3.
- Pseudo-code Backtracking.
- Bảng nghiệm 5 nhà.
- Kết luận:
  - Người nuôi Zebra là `Japanese`.
  - Người uống Water là `Norwegian`.

## Kiểm tra trước khi nộp

Chạy:

```powershell
python -m unittest
python src/einstein_csp.py
```

Nếu cả hai lệnh đều chạy thành công và kết quả cuối đúng, phần code đã sẵn sàng để đưa vào báo cáo.
