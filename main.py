#пишем функцию sum_range(start, end)
def sum_range(start, end):
  # Функция суммирует все целые числа от start до end
  total = 0
  for num in range(start, end+1):
      total += num
  return total

# Пример
start_value = 1
end_value = 52
result = sum_range(start_value, end_value)
print(f"Сумма всех целых чисел от {start_value} до {end_value} равна: {result}")


print("Hello, World!")