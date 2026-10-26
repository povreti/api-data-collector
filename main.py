import logging
from api_client import fetch_users
from data_manager import load_users, update_users


path = 'users.json'
https_path = 'https://jsonplaceholder.typicode.com/users'


logging.basicConfig(
    filename='Logs/main.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


if __name__ == '__main__':
    users = fetch_users(https_path)
    saved_users = load_users(path)
    if saved_users and users:
        update_users(path, saved_users, users)
    logging.info('Конец программы\n')