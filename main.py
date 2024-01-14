from mod import number_guessing_game
import math


def calculate_z(m, n):
  try:
    result = (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)
    return result
  except ValueError:
    return "Неможливо обчислити. Перевірте значення m та n."

if __name__ == "__main__":
  m = float(input("Введіть значення m: "))
  n = float(input("Введіть значення n: "))

  result_z = calculate_z(m, n)
  print(f"Результат обчислення z: {result_z}")
  number_guessing_game()
  
