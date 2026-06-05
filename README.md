# Einstein's Riddle CSP Solver

Repo này triển khai bài tập **3.3 Einstein's Riddle (The Zebra Puzzle)** bằng mô hình CSP. Chương trình dùng AC-3 để cắt miền trước, sau đó dùng Backtracking với MRV để tìm nghiệm đầy đủ.

## Mục tiêu bài

Bài toán có 5 ngôi nhà. Mỗi nhà có một màu, một quốc tịch, một đồ uống, một loại thuốc lá và một thú cưng. Không có hai nhà nào trùng giá trị trong cùng một nhóm thuộc tính.

Yêu cầu chính của đề:

- Mô hình hóa bài toán dưới dạng CSP.
- Dùng AC-3.
- Dùng Backtracking.
- Trả lời:
  - Ai nuôi Zebra?
  - Ai uống Water?

## Cách chạy

```powershell
python src/einstein_csp.py
```

Nếu Windows chưa nhận lệnh `python`, thử:

```powershell
py -3 src/einstein_csp.py
```

Kết quả đúng cần thấy:

```text
Who owns the Zebra? Japanese
Who drinks Water? Norwegian
```

## Cách chạy test

```powershell
python -m unittest
```

Lệnh dự phòng trên Windows:

```powershell
py -3 -m unittest
```

## Cấu trúc repo

- `src/einstein_csp.py`: code CSP, constraints, AC-3, Backtracking và in nghiệm.
- `tests/test_einstein_csp.py`: test ràng buộc tương đối, All-Different, AC-3 và nghiệm cuối.
- `docs/khac_truong.md`: phần Khắc Trường phụ trách để đưa vào báo cáo.
- `docs/next_steps.md`: hướng dẫn các phần kế tiếp cho các nhóm còn lại.

## Mô hình CSP

Code biểu diễn mỗi thuộc tính là một biến vị trí nhà. Ví dụ:

- `Norwegian = 1`: người Na Uy ở nhà đầu tiên.
- `Milk = 3`: sữa được uống ở nhà giữa.
- `Green = Ivory + 1`: nhà xanh lá nằm ngay bên phải nhà màu ngà.
- `abs(Kools - Horse) == 1`: nhà hút Kools nằm cạnh nhà nuôi ngựa.

Miền giá trị của mọi biến là `{1, 2, 3, 4, 5}`.

## Phần Khắc Trường cần tập trung

Trong `src/einstein_csp.py`, phần quan trọng nhất là:

- `build_relative_constraints()`: clue 5, 10, 11, 14, 15.
- `build_all_different_constraints()`: không cho trùng màu, quốc tịch, đồ uống, thuốc lá, thú cưng.
- `immediate_right()` và `next_to()`: hai công thức xử lý vị trí tương đối giữa các nhà.
