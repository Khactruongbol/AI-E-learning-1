# Einstein's Zebra Puzzle – Backtracking & MRV

## Thành viên thực hiện

| Nguyễn Văn Đức | Phân tích cây không gian trạng thái, xây dựng thuật toán Backtracking |
| Trương Tuấn Dũng | Nghiên cứu và cài đặt heuristic MRV (Minimum Remaining Values), kiểm thử chương trình |

---

## Tổng quan nhiệm vụ

Phần Backtracking & MRV là một trong những phần quan trọng nhất của bài toán Einstein's Zebra Puzzle. Đây là giai đoạn thực hiện tìm kiếm nghiệm sau khi bài toán đã được mô hình hóa dưới dạng CSP (Constraint Satisfaction Problem).

Mục tiêu của nhóm là xây dựng một thuật toán có khả năng:

- Tìm ra nghiệm thỏa mãn toàn bộ 15 manh mối của bài toán.
- Giảm số lượng trạng thái cần duyệt.
- Tăng hiệu quả tìm kiếm bằng các heuristic phù hợp.
- Trả lời chính xác hai câu hỏi cuối cùng:
  - Ai là người sở hữu Zebra?
  - Ai là người uống nước?

---

# Phần việc của Nguyễn Văn Đức

## 1. Phân tích cây không gian trạng thái

Nguyễn Văn Đức chịu trách nhiệm nghiên cứu cách biểu diễn bài toán dưới dạng cây tìm kiếm.

Mỗi nút trong cây biểu diễn:

- Một trạng thái gán giá trị tạm thời cho các biến.
- Một tập các ràng buộc cần được thỏa mãn.
- Một bước tiến gần hơn tới nghiệm hoàn chỉnh.

Thông qua việc phân tích cây trạng thái, nhóm xác định được:

- Thứ tự tìm kiếm.
- Điều kiện quay lui.
- Điều kiện kết thúc.
- Các trường hợp cần cắt tỉa nhánh.

---

## 2. Xây dựng thuật toán Backtracking

Nguyễn Văn Đức thiết kế bộ khung đệ quy cho quá trình tìm kiếm.

Thuật toán hoạt động theo các bước:

1. Chọn một biến chưa được gán.
2. Thử lần lượt các giá trị trong miền giá trị.
3. Kiểm tra tính hợp lệ của các ràng buộc.
4. Nếu hợp lệ thì tiếp tục tìm kiếm.
5. Nếu không hợp lệ thì quay lui (Backtrack).
6. Kết thúc khi tất cả biến đều được gán giá trị.

Ý tưởng chính:

```python
assignment[var] = value

if check_constraints(assignment):
    result = backtrack(assignment)
```

Backtracking đóng vai trò là nền tảng chính của toàn bộ chương trình.

---

# Phần việc của Trương Tuấn Dũng

## 1. Nghiên cứu heuristic MRV

Trương Tuấn Dũng phụ trách nghiên cứu và áp dụng kỹ thuật MRV (Minimum Remaining Values).

MRV là một heuristic phổ biến trong các bài toán CSP nhằm lựa chọn biến có số lượng giá trị hợp lệ còn lại ít nhất.

Ý tưởng:

- Ưu tiên xử lý biến khó trước.
- Phát hiện thất bại sớm.
- Giảm số lượng nhánh cần duyệt.

---

## 2. Cài đặt cơ chế lựa chọn biến thông minh

MRV được tích hợp thông qua hàm:

```python
def select_unassigned_variable(assignment):

    unassigned = [
        v for v in variables
        if v not in assignment
    ]

    return min(
        unassigned,
        key=lambda v: len(domains[v])
    )
```

Chức năng:

- Tìm các biến chưa được gán.
- So sánh số lượng giá trị còn lại trong miền giá trị.
- Chọn biến có miền nhỏ nhất.

---

## 3. Tối ưu quá trình tìm kiếm

Việc sử dụng MRV giúp:

- Giảm đáng kể số lượng trạng thái cần kiểm tra.
- Hạn chế việc duyệt các nhánh không khả thi.
- Tăng tốc quá trình tìm kiếm nghiệm.

Thay vì chọn biến ngẫu nhiên, MRV tập trung vào các biến có khả năng gây xung đột cao nhất.

---

## 4. Kiểm thử chương trình

Trương Tuấn Dũng thực hiện:

- Kiểm tra tính đúng đắn của thuật toán.
- Kiểm tra kết quả cuối cùng.
- Đối chiếu nghiệm với đáp án chuẩn của Einstein's Zebra Puzzle.

Kết quả thu được:

```text
Owner of Zebra : Japanese
Drinks Water   : Norwegian
```

---

# Thuật toán sử dụng

## Backtracking

Đặc điểm:

- Tìm kiếm theo chiều sâu (Depth First Search).
- Thử và sửa.
- Quay lui khi gặp trạng thái không hợp lệ.

Ưu điểm:

- Dễ cài đặt.
- Đảm bảo tìm được nghiệm nếu tồn tại.

---

## MRV (Minimum Remaining Values)

Đặc điểm:

- Là heuristic chọn biến.
- Ưu tiên biến có ít lựa chọn nhất.
- Phát hiện xung đột sớm.

Ưu điểm:

- Giảm không gian tìm kiếm.
- Tăng hiệu suất thực thi.
- Hạn chế số lần quay lui.

---

# Kết quả đạt được

Chương trình đã:

- Mô hình hóa thành công bài toán dưới dạng CSP.
- Áp dụng Backtracking để tìm nghiệm.
- Tích hợp heuristic MRV nhằm tối ưu tìm kiếm.
- Tìm được nghiệm chính xác cho Einstein's Zebra Puzzle.

Kết quả cuối cùng:

```text
Owner of Zebra : Japanese
Drinks Water   : Norwegian
```

---

# Kết luận

Thông qua việc kết hợp Backtracking và MRV, nhóm đã xây dựng thành công chương trình giải Einstein's Zebra Puzzle.

Nguyễn Văn Đức tập trung vào việc phân tích cây không gian trạng thái và xây dựng thuật toán Backtracking, trong khi Trương Tuấn Dũng phụ trách nghiên cứu, cài đặt và tối ưu quá trình lựa chọn biến bằng heuristic MRV.

Sự kết hợp giữa hai phần giúp giảm đáng kể số lượng trạng thái cần duyệt và tìm được nghiệm chính xác cho bài toán.