import random


def number_guessing_game():
  secret_number = random.randint(1, 100)
  user_guess = 0

  while user_guess != secret_number:
    try:
      user_guess = int(input("Введіть своє число від 1 до 100: "))

      if user_guess < secret_number:
        print("Моє число більше.")
      elif user_guess > secret_number:
        print("Моє число менше.")
      else:
        print("Ви вгадали!")
    except ValueError:
      print("Будь ласка, введіть правильне ціле число.")


if __name__ == "__main__":
  number_guessing_game()
