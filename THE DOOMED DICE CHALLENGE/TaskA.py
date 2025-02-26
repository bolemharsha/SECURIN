from collections import defaultdict
import itertools

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

sum_counts = defaultdict(int)

for a, b in itertools.product(Die_A, Die_B):
    sum_counts[a + b] += 1

total_combinations = 6 * 6 
probabilities = {s: count / total_combinations for s, count in sum_counts.items()}

print("Total Combinations:", total_combinations)
print("Sum Distribution:", dict(sum_counts))
print("Probability Distribution:", probabilities)
