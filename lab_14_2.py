import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо CSV-файл з даними
file_path = "data_file.csv"  # Замініть це на шлях до вашого файлу
data = pd.read_csv(file_path)

# Вибираємо країни для аналізу (наприклад, Україну та США)
countries_to_analyze = ['Ukraine', 'United States']

# Вводимо роки для аналізу
years_to_analyze = ['2000 [YR2000]', '2005 [YR2005]', '2010 [YR2010]', '2015 [YR2015]', '2019 [YR2019]']

# Вибираємо дані для візуалізації
selected_data = data[data['Country Name'].isin(countries_to_analyze)][['Country Name'] + years_to_analyze]

# Побудова графіку ліній
plt.figure(figsize=(10, 6))
for country in countries_to_analyze:
    country_data = selected_data[selected_data['Country Name'] == country]
    plt.plot(country_data.columns[1:], country_data.values[0][1:], label=country)

plt.title('Динаміка показника для обраних країн')
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.legend()
plt.show()

# Побудова стовпчатої діаграми
user_country = input("Введіть назву країни для побудови стовпчатої діаграми: ")
user_country_data = selected_data[selected_data['Country Name'] == user_country].values[0][1:]

plt.figure(figsize=(8, 5))
plt.bar(years_to_analyze, user_country_data, color='blue')
plt.title(f'Значення показника для {user_country} за обрані роки')
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.show()
