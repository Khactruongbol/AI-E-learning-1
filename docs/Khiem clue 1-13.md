# Khởi tạo Dữ liệu & Ràng buộc Cơ bản

**Thành viên thực hiện:** Nguyễn Vĩnh Khiêm (Phân tích biểu thức logic cho các Ràng buộc nhị phân: Clue 1, 2, 3, 4, 6, 7, 12, 13).

---

### 4. Phân tích Ràng buộc nhị phân (Binary Constraints)

Ràng buộc nhị phân là các điều kiện thiết lập mối quan hệ tương quan trực tiếp giữa hai thuộc tính khác nhau của cùng một ngôi nhà. Trong mô hình bài toán này, vì ta coi vị trí của ngôi nhà (từ 1 đến 5) là miền giá trị của các biến thuộc tính, nên các ràng buộc nhị phân thể hiện rằng hai thuộc tính này phải có cùng một giá trị vị trí ngôi nhà.

Dưới đây là phần phân tích chi tiết và biểu diễn logic cho các ràng buộc nhị phân được phân công (gồm các Clue 1, 2, 3, 4, 6, 7, 12, 13):

* **Clue 1:** *"The Brit lives in the Red house."* (Người Anh sống trong ngôi nhà màu Đỏ)
    * **Phân tích:** Nếu một ngôi nhà có thuộc tính Quốc tịch là `Brit` thì thuộc tính Màu sắc của ngôi nhà đó phải là `Red`, và ngược lại. Do đó, hai biến này phải nhận cùng một giá trị số nhà.
    * **Biểu diễn logic:** $Brit = Red$

* **Clue 2:** *"The Spaniard owns the Dog."* (Người Tây Ban Nha nuôi Chó)
    * **Phân tích:** Vị trí ngôi nhà của người có Quốc tịch `Spaniard` phải trùng với vị trí ngôi nhà có Thú cưng là `Dog`.
    * **Biểu diễn logic:** $Spaniard = Dog$

* **Clue 3:** *"Coffee is drunk in the Green house."* (Cà phê được uống trong ngôi nhà màu Xanh lá)
    * **Phân tích:** Biến thuộc tính Đồ uống `Coffee` và biến thuộc tính Màu sắc `Green` phải có giá trị bằng nhau.
    * **Biểu diễn logic:** $Coffee = Green$

* **Clue 4:** *"The Ukrainian drinks Tea."* (Người Ukraina uống Trà)
    * **Phân tích:** Ngôi nhà có thuộc tính Quốc tịch là `Ukrainian` đồng thời phải có thuộc tính Đồ uống là `Tea`.
    * **Biểu diễn logic:** $Ukrainian = Tea$

* **Clue 6:** *"The Old Gold smoker owns Snails."* (Người hút thuốc lá Old Gold nuôi Ốc sên)
    * **Phân tích:** Biến Thuốc lá `Old_Gold` và biến Thú cưng `Snails` được ràng buộc chung một vị trí ngôi nhà.
    * **Biểu diễn logic:** $Old\_Gold = Snails$

* **Clue 7:** *"Kools are smoked in the Yellow house."* (Thuốc lá Kools được hút ở ngôi nhà màu Vàng)
    * **Phân tích:** Ngôi nhà nơi biến Thuốc lá bằng `Kools` phải chính là ngôi nhà có biến Màu sắc bằng `Yellow`.
    * **Biểu diễn logic:** $Kools = Yellow$

* **Clue 12:** *"The Lucky Strike smoker drinks Orange Juice."* (Người hút thuốc lá Lucky Strike uống Nước cam)
    * **Phân tích:** Giá trị vị trí của biến Thuốc lá `Lucky_Strike` phải tương đương với biến Đồ uống `Orange_Juice`.
    * **Biểu diễn logic:** $Lucky\_Strike = Orange\_Juice$

* **Clue 13:** *"The Japanese smokes Parliaments."* (Người Nhật Bản hút thuốc lá Parliaments)
    * **Phân tích:** Ngôi nhà có biến Quốc tịch là `Japanese` sẽ có cùng số thứ tự với ngôi nhà có biến Thuốc lá là `Parliaments`.
    * **Biểu diễn logic:** $Japanese = Parliaments$

---

Nhờ các ràng buộc nhị phân này, không gian tìm kiếm sẽ được thu hẹp đáng kể khi thuật toán **AC-3** thực hiện lọc và đồng bộ hóa miền giá trị (*domain consistency*) giữa các cặp biến với nhau trước và trong quá trình **Backtracking**.
