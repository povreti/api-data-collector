import requests  
import logging

def fetch_users(https_path):
    try:
        response = requests.get(
            https_path,
            timeout=10
            )
        response.raise_for_status()        
        users = response.json()
        return users

    except requests.exceptions.RequestException:
        logging.error('Ошибка чтения запроса')
        return None