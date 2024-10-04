import time
import logging
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')
        logging.info(f'El nombre del pokemon es {name}')
        

def show_user_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('results')[0].get('name').get('first')
        logging.info(f'El nombre del usuario es {name}')

def generate_request(url):
    return requests.get(url)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='Hilo') as executor:

        future_pokemon = executor.submit(generate_request, 'https://pokeapi.co/api/v2/pokemon/1/')
        future_user = executor.submit(generate_request, 'https://randomuser.me/api')

        future_pokemon.add_done_callback(
            lambda response: show_pokemon_name(response.result())
        )
        future_user.add_done_callback(
            lambda response: show_user_name(response.result())
        )
        