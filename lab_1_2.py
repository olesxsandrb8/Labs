def find_and_print_multiples():
  start_range = 30
  end_range = 60
  multiples_of_three = [num for num in range(start_range, end_range + 1) if num % 3 == 0]

  if multiples_of_three:
      print(f"Цілі числа, кратні трьом в діапазоні від {start_range} до {end_range}:")
      for number in multiples_of_three:
          print(number, end=" ")
      print(f"\nКількість таких чисел: {len(multiples_of_three)}")
  else:
      print(f"У діапазоні від {start_range} до {end_range} немає цілих чисел, кратних трьом.")

if __name__ == "__main__":
  find_and_print_multiples()
