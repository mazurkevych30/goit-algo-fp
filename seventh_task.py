import numpy as np

def monte_carlo(n):
    first_cube = np.random.randint(1, 7, n)
    second_cube = np.random.randint(1, 7, n)

    unique_numbers, counts = np.unique(first_cube + second_cube, return_counts=True)
    percentages = (counts / n) * 100

    return list(zip(unique_numbers, percentages))

res = monte_carlo(10000)


print(f"{'Число':<2}\t|\t{'Відсоток випадіння (%)':<2}")
print("-" * 45)

for number, percentage in res:
    print(f"{number:<2}\t|\t{percentage:<2.2f}")
