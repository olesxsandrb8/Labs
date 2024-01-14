def is_fibonacci(num):
  a, b = 0, 1
  while a < num:
      a, b = b, a + b
  return a == num

# Задана множина цілих чисел від 1 до 50
numbers_set = set(range(1, 51))

# Знаходимо числа Фібоначчі у множині
fibonacci_numbers = {num for num in numbers_set if is_fibonacci(num)}

# Виводимо результат на екран
print("Множина чисел Фібоначчі:", fibonacci_numbers)
