conjuntos_even_ = set((c**2, c**3) for c in range(10) if c%2 == 0)
conjuntos_even = sorted(conjuntos_even_, key=lambda x: x[1])
# Output: [(0, 0), (4, 8), (16, 64), (36, 216), (64, 512)]

conjuntos_odd_ = set((c**2, c**3) for c in range(10) if c%2 != 0)
conjuntos_odd = sorted(conjuntos_odd_, key=lambda x: x[1])
# Output: [(1, 1), (9, 27), (25, 125), (49, 343), (81, 729)]

conjuntos_even_.update(conjuntos_odd_)
conjuntos_even = sorted(conjuntos_even_, key=lambda x: x[1])
print(conjuntos_even)
# Output: [(0, 0), (1, 1), (4, 8), (9, 27), (16, 64), 
# (25, 125), (36, 216), (49, 343), (64, 512), (81, 729)]


set_div_3 = set(
    (c**2, c**3) for c in range(10) if c%3 == 0
)

print(
    set_div_3 | conjuntos_odd_
)
# Output: {(0, 0), (1, 1), (9, 27), (36, 216), (81, 729), (25, 125), (49, 343)}
print(
    set_div_3 & conjuntos_odd_
)
# Output: {(9, 27), (81, 729)}
print(
    set_div_3 - conjuntos_odd_
)
# Output: {(0, 0), (36, 216)}
print(
    set_div_3 ^ conjuntos_odd_
)
# Output: {(0, 0), (1, 1), (25, 125), (36, 216), (49, 343), (81, 729)}




