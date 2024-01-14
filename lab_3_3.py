def swap_first_and_last_words(sentence):
  words = sentence.split()

  if len(words) >= 2:
    # міняємо місцями перше та останнє слово
    words[0], words[-1] = words[-1], words[0]

    # Збираємо знову речення
    modified_sentence = ' '.join(words)

    return modified_sentence
  else:
    return sentence


# Зчитуємо речення з користувача (можна також ввести речення безпосередньо в коді)
sentence = input("Введіть речення: ")
modified_sentence = swap_first_and_last_words(sentence)
print("Змінене речення:", modified_sentence)
