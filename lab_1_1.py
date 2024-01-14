def calculate_x(a, b):
  if a > b:
      x = a * b + 1
  elif a == b:
      x = 25
  else:
      x = (a - 5) / b
  return x

def main():
  try:
      a = float(input("Введіть значення a (додатнє число): "))
      b = float(input("Введіть значення b (додатнє число): "))

      if a <= 0 or b <= 0:
          print("Будь ласка, введіть лише додатні числа.")
      else:
          result = calculate_x(a, b)
          print(f"Результат обчислення x: {result}")
  except ValueError:
      print("Будь ласка, введіть числові значення.")

if __name__ == "__main__":
  main()
