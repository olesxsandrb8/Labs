import math
import random

def calculate_z(m, n):
    try:
        result = (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)
        return result
    except ValueError:
        return "Неможливо обчислити. Перевірте значення m та n."

def guess_the_number():
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
    m = float(input("Введіть значення m: "))
    n = float(input("Введіть значення n: "))

    result_z = calculate_z(m, n)
    print(f"Результат обчислення z: {result_z}")

    guess_the_number()
