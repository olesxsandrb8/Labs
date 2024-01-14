def fibon (n):
  f = [1, 1]  # Початкові значення послідовності Фібоначчі

  # Генеруємо n-2 елементів послідовності (вже є два початкові)
  for i in range(2, n):
      next_element = f[-1] + f[-2]
      f.append(next_element)

  return f

n = int(input("Введіть кількість елементів у послідовності Фібоначчі: "))

fibonacci_array = fibon(n)

print(f"Перші {n} елементів послідовності Фібоначчі:")
print(fibonacci_array)
