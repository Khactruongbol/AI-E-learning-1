from collections import deque

# --- KHỞI TẠO DỮ LIỆU (PHƯƠNG UYÊN) ---
queue = deque([
    ("X1", "X2"),
    ("X2", "X1"),
    ("X2", "X3"),
    ("X3", "X2")
])

domains = {
    "X1": [1, 2, 3],
    "X2": [1, 2, 3],
    "X3": [1, 2, 3]
}

neighbors = {
    "X1": ["X2"],
    "X2": ["X1", "X3"],
    "X3": ["X2"]
}


# --- LOGIC THUẬT TOÁN AC-3 (LÂM HƯNG) ---
def satisfies_constraint(x, y, Xi, Xj):
    # Kiểm tra ràng buộc mẫu X1 < X2 và X2 < X3
    if Xi == "X1" and Xj == "X2": return x < y
    if Xi == "X2" and Xj == "X1": return x > y
    if Xi == "X2" and Xj == "X3": return x < y
    if Xi == "X3" and Xj == "X2": return x > y
    return True

def revise(Xi, Xj, domains):
    revised = False
    for x in domains[Xi][:]:
        # Nếu không có giá trị y nào thỏa mãn ràng buộc với x
        if not any(satisfies_constraint(x, y, Xi, Xj) for y in domains[Xj]):
            domains[Xi].remove(x)
            revised = True
    return revised

def ac3(queue, domains, neighbors):
    while queue:
        Xi, Xj = queue.popleft()
        if revise(Xi, Xj, domains):
            if len(domains[Xi]) == 0:
                return False
            # Thêm lại các cung láng giềng liên quan (trừ Xj)
            for Xk in neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True


if __name__ == "__main__":
    print("Miền giá trị trước AC-3:", domains)
    if ac3(queue, domains, neighbors):
        print("Miền giá trị sau AC-3: ", domains)
    else:
        print("Bài toán vô nghiệm.")