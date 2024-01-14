def qsort(lst):
  if len(lst) <= 1:
      return lst
  else:
      pivot, *rest = lst
      less = [x for x in rest if x <= pivot]
      greater = [x for x in rest if x > pivot]
      return qsort(less) + [pivot] + qsort(greater)

user_lst = [int(x) for x in input("Введіть елементи списку через пробіл: ").split()]
sorted_lst = qsort(user_lst)

print("Відсортований список:", sorted_lst)
