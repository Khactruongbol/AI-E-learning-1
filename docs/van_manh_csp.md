## Khởi tạo Dữ liệu & Ràng buộc Cơ bản

### 1. Định nghĩa không gian bài toán CSP
Bài toán Câu đố Einstein (Zebra Puzzle) được mô hình hóa theo cấu trúc của một bài toán Thỏa mãn Ràng buộc (Constraint Satisfaction Problem - CSP). Về mặt toán học, bài toán được biểu diễn bằng một bộ ba $P = (X, D, C)$, trong đó:
*   **$X$ (Variables):** Tập hợp các biến số đại diện cho các đặc tính cần tìm hiểu.
*   **$D$ (Domains):** Miền giá trị hữu hạn mà các biến số trong $X$ có thể nhận.
*   **$C$ (Constraints):** Tập hợp các ràng buộc giới hạn sự kết hợp giá trị giữa các biến.

### 2. Phân tích Biến số ($X$) và Miền giá trị ($D$)
Thay vì coi 5 ngôi nhà là các biến, cách tiếp cận tối ưu hơn để giảm thiểu độ phức tạp cho thuật toán là coi **các thuộc tính của người thuê nhà là biến số**, và **vị trí của ngôi nhà (từ 1 đến 5) là miền giá trị**.

*   **Miền giá trị chung ($D$):** 
    Cả 25 biến số đều chia sẻ chung một không gian tìm kiếm là vị trí rời rạc của 5 ngôi nhà xếp thẳng hàng.
    $$D = \{1, 2, 3, 4, 5\}$$

*   **Tập hợp 25 biến số ($X$):**
    Dựa trên dữ kiện đề bài, ta định nghĩa 25 biến số, được phân hoạch thành 5 nhóm thuộc tính độc lập:
    1.  **Nhóm Màu sắc (Color):** $Red, Green, Ivory, Yellow, Blue$
    2.  **Nhóm Quốc tịch (Nationality):** $Brit, Spaniard, Ukrainian, Norwegian, Japanese$
    3.  **Nhóm Đồ uống (Drink):** $Coffee, Tea, Milk, OrangeJuice, Water$
    4.  **Nhóm Thuốc lá (Smoke):** $OldGold, Kools, Chesterfields, LuckyStrike, Parliaments$
    5.  **Nhóm Thú cưng (Pet):** $Dog, Snails, Fox, Horse, Zebra$

    **Ràng buộc ngầm định (AllDiff):** Bất kỳ 2 biến nào thuộc cùng một nhóm thuộc tính đều không được nhận cùng một giá trị (ví dụ: Không thể có 2 người cùng quốc tịch hoặc 2 nhà cùng màu).

### 3. Phân tích Ràng buộc Đơn phân (Unary Constraints)
Ràng buộc đơn phân là các điều kiện tiên quyết tác động độc lập lên một biến duy nhất. Trong bài toán này, các ràng buộc đơn phân đóng vai trò cực kỳ quan trọng trong việc cắt tỉa (pruning) không gian tìm kiếm ngay từ bước khởi tạo, bằng cách giới hạn chặt miền giá trị của biến đó về một phần tử duy nhất.

Trích xuất từ tập luật của bài toán, ta có 2 ràng buộc đơn phân:
*   **Clue 8:** *"Milk is drunk in the middle house."*
    *   **Phân tích:** Thuộc tính Đồ uống (Milk) được cố định tại ngôi nhà số 3.
    *   **Biểu diễn logic:** $Milk = 3$
*   **Clue 9:** *"The Norwegian lives in the first house."*
    *   **Phân tích:** Thuộc tính Quốc tịch (Norwegian) được cố định tại ngôi nhà số 1.
    *   **Biểu diễn logic:** $Norwegian = 1$
    
Nhờ 2 ràng buộc này, thuật toán sẽ không phải duyệt qua các hoán vị sai lệch của biến $Milk$ và $Norwegian$, giúp tăng tốc độ hội tụ của hệ thống.