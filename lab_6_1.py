def insert_after_element(lst, element, new_element):
  try:
      index = lst.index(element)
      lst.insert(index + 1, new_element)
      print(f"{new_element} вставлено після {element}.")
  except ValueError:
      print(f"{element} не знайдено у списку.")

user_list = [int(x) for x in input("Введіть елементи списку через пробіл: ").split()]
element_to_find = int(input("Введіть елемент, після якого потрібно вставити новий елемент: "))
new_element_to_insert = int(input("Введіть новий елемент для вставки: "))

insert_after_element(user_list, element_to_find, new_element_to_insert)

print("Оновлений список:", user_list)
