def square_numbers(numbers): # Функция для возведения чисел в квадрат
    return [number ** 2 for number in numbers]
input_numbers = [4, 13, 8, 5, 11] # Пример использования функции
squared_numbers = square_numbers(input_numbers)
print("Исходный список:", input_numbers) #Вывод
print("Список квадратов:", squared_numbers)
