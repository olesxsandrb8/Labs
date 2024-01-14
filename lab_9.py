# a) Створення файлу TF1_1 з символьних рядків
with open('TF1_1.txt', 'w') as file_tf1_1:
    file_tf1_1.write("Привіт світ !\n")
    file_tf1_1.write("Погода сьогодні похмура.\n")
    file_tf1_1.write("Але чай та серіал зіргріває)\n")

# b) Читання вмісту файла TF1_1 і запис кожного слова в окремий рядок файла TF1_2
with open('TF1_1.txt', 'r') as file_tf1_1, open('TF1_2.txt', 'w') as file_tf1_2:
    for line in file_tf1_1:
        words = line.split()
        for word in words:
            file_tf1_2.write(word + '\n')

# c) Читання вмісту файла TF1_2 і друк по рядках
with open('TF1_2.txt', 'r') as file_tf1_2:
    print("Вміст файла TF1_2:")
    for line in file_tf1_2:
        print(line.strip())
