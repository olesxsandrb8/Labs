def create_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Файл {filename} успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу {filename}: {e}")

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            # Читання вмісту файла та розділення його на слова
            words = [word.strip('.,;?!') for line in input_file for word in line.split()]

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            # Запис кожного слова в окремий рядок файла TF1_2
            for word in words:
                output_file.write(word + '\n')

        print(f"Файл {output_filename} успішно створено.")

    except FileNotFoundError:
        print(f"Помилка: Файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при обробці файлів: {e}")

def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Виведення вмісту файла по рядках
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу {filename}: {e}")

# а) Створення текстового файлу TF1_1
create_file("TF1_1.txt", "Слова різної довжини та розділові знаки! Це файл для завдання.")

# б) Читання вмісту файла TF1_1 та запис кожного слова в окремий рядок файла TF1_2
process_file("TF1_1.txt", "TF1_2.txt")

# в) Читання та виведення вмісту файла TF1_2 по рядках
print_file_content("TF1_2.txt")
