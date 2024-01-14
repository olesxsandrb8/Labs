def print_pattern(N):
  for i in range(N, 0, -1):
      for k in range(i, N + 1):
          print(k, end=" ")
      print()

if __name__ == "__main__":
  try:
      N = int(input("Введіть ціле число N (1 < N < 9): "))
      if 1 < N < 9:
          print_pattern(N)
      else:
          print("Введене число не входить в діапазон (1 < N < 9).")
  except ValueError:
      print("Будь ласка, введіть правильне ціле число.")
