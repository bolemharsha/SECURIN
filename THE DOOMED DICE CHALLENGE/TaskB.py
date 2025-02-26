from collections import defaultdict
import itertools

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

sum_counts = defaultdict(int)
def undoom_dice(original_A, original_B):
    sum_counts = defaultdict(int)

    for a, b in itertools.product(original_A, original_B):
        sum_counts[a + b] += 1

    New_Die_A = [1, 2, 2, 3, 3, 4] 
    New_Die_B = [0] * 6

    for a in New_Die_A:
        for b in range(1, 21):
            if sum_counts.get(a + b, 0) > 0:
                New_Die_B[New_Die_A.index(a)] = b
                sum_counts[a + b] -= 1
                break

    return New_Die_A, New_Die_B

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
