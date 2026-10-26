import json
import logging


def save_users(users, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)
        return True

    except OSError:
        logging.error('Возникла проблема c записью файла')
        return False


def load_users(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            saved_users = json.load(file)
        return saved_users

    except FileNotFoundError:
        logging.error('Файл не найден')
        return None

    except json.JSONDecodeError:
        logging.error('Содержание файла не удалось разобрать')
        return None


def update_users(path, saved_users, users):
    if saved_users == users:
        logging.info('Данные не изменились')

    else:
        if save_users(users, path):
            logging.info('Данные успешно обновлены')