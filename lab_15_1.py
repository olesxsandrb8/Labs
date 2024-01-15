import pandas as pd
import numpy as np

def count_fibonacci_numbers(numbers):
    fibonacci_set = set()
    a, b = 0, 1
    while b <= max(numbers):
        fibonacci_set.add(b)
        a, b = b, a + b

    count = len(set(numbers) & fibonacci_set)
    return count

data = {
    'Number': list(range(1, 51)),
    'Square': [x**2 for x in range(1, 51)],
}

data['IsFibonacci'] = count_fibonacci_numbers(data['Number'])

df = pd.DataFrame(data)

print("Датафрейм:")
print(df)

aggregated_data = df.groupby('IsFibonacci').agg({
    'Number': 'count',
    'Square': 'sum',
})
print("\nАгреговані дані:")
print(aggregated_data)
