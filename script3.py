def get_cost(weight: int):
    # Напишите здесь свой код для задания, используйте конструкцию вывода как в примере выше
    if weight <= 10:
        return 'Стоимость доставки: 200 руб.'
    elif weight > 10:
        return 'Стоимость доставки: 500 руб.'
if __name__ == '__main__':
    # Этот код менять не надо
    delivery = get_cost(9)
    assert '200' in delivery, "Стоимость доставки должна быть 200 руб. если вес 9 кг"
    print('Вес посылки 9 кг', delivery)
    delivery = get_cost(12)
    assert '500' in delivery, "Стоимость доставки должна быть 500 руб. если вес 12 кг"
    print('Вес посылки 12 кг', delivery)
