import json


def save_users(users, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    except OSError:
        print('Возникла проблема c записью файла')


def load_users(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            saved_users = json.load(file)
        return saved_users

    except FileNotFoundError:
        print('Файл не найден')
        return None

    except json.JSONDecodeError:
        print('Содержание файла не удалось разобрать')
        return None


def update_users(path, saved_users, users):
    try:
        if saved_users == users:
            print('Данные не изменились')

        else:
            save_users(users, path)
            print('Данные успешно обновлены')
    
    except OSError:
        print('Ошибка при записи файла')