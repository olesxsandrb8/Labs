def find_longest_sequence(word):
  max_count = 0
  current_count = 1
  max_char = None

  for i in range(1, len(word)):
      if word[i] == word[i - 1]:
          current_count += 1
      else:
          if current_count > max_count:
              max_count = current_count
              max_char = word[i - 1]
          current_count = 1

  # Перевірка для останнього символу
  if current_count > max_count:
      max_count = current_count
      max_char = word[-1]

  return max_char, max_count

word = input("Введіть слово: ")

# Визначаємо та виводимо результат
max_char, max_count = find_longest_sequence(word)
if max_count > 1:
  print(f"Найбільша кількість однакових символів підряд - '{max_char}', кількість: {max_count}")
else:
  print("У слові немає однакових символів підряд.")
