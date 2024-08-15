def check_triangle(side1: int, side2: int, side3: int):
    """Дополните код ниже"""
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        result = "Треугольник не существует"
    elif side1 == side2 == side3:
        result = "Равносторонний треугольник"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result


if __name__ == '__main__':
    # Этот код менять не надо
    triangle = check_triangle(10, 10, 10)
    assert triangle == 'Равносторонний треугольник', f"Получен неверный ответ: {triangle}"
    print("Треугольник со сторонами 10, 10, 10:", triangle)
    triangle = check_triangle(10, 20, 30)
    assert triangle == "Треугольник не существует", f"Получен неверный ответ: {triangle}"
    print("Треугольник со сторонами 10, 20, 30:", triangle)
    triangle = check_triangle(10, 10, 20)
    assert check_triangle(10, 10, 20) == "Треугольник не существует", f"Получен неверный ответ: {triangle}"
    print("Треугольник со сторонами 10, 10, 20:", triangle)
    triangle = check_triangle(-10, 10, 20)
    assert triangle == 'Треугольник не существует', f"Получен неверный ответ: {triangle}"
    print("Треугольник со сторонами -10, 10, 20:", triangle)