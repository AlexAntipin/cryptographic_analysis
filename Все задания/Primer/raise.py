def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:

        y = 1
        # Выполняем действия, например, выводим сообщение об ошибке
        print(f"Произошла ошибка: {str(e)}")
        # Повторно возбуждаем исключение
        raise
    else:
        return result

# Вызываем функцию divide с параметрами 10 и 0, что вызовет исключение ZeroDivisionError
result = divide(10, 0)

