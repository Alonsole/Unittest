def check_auth(login: str, password: str):

    if login == "admin" and password == "password":
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'

    return result


if __name__ == '__main__':
    auth = check_auth('user', 'password')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный login:', auth)

    auth = check_auth('admin', '123')
    assert auth == 'Доступ ограничен', f'Получен неверный ответ: {auth}'
    print('Неверный password:', auth)

    auth = check_auth('admin', 'password')
    assert auth == 'Доброf пожаловать', f'Получен неверный ответ: {auth}'
    print('Верные login, password:', auth)
