import requests  


def fetch_users():
    try:
        response = requests.get(
            'https://jsonplaceholder.typicode.com/users',
            timeout=10
            )
        response.raise_for_status()        
        users = response.json()
        return users

    except requests.exceptions.RequestException:
        print('Ошибка чтения запроса')
        return None