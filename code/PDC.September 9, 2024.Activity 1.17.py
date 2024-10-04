import logging
import requests
import threading
from concurrent.futures import Future

logging.basicConfig(level=logging.INFO, format='%(message)s')

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
    future_response = Future()
    thread = threading.Thread(target=(
        lambda: future_response.set_result(requests.get(url))
    ))
    thread.start()
    return future_response


if __name__ == '__main__':
    future_response = generate_request('https://pokeapi.co/api/v2/pokemon/1/')
    future_response_user=generate_request('https://randomuser.me/api')
    future_response.add_done_callback(
        lambda future_response: show_pokemon_name(future_response.result())
    )
    future_response.add_done_callback(
        lambda future_response: show_pokemon_name(future_response.result())
    )
    future_response_user.add_done_callback(
        lambda future_response: show_user_name(future_response.result())
    )
    while (not future_response.done() or future_response_user.done()):
        logging.info('Esperando resultados')
    else:
        logging.info('Fin del programa!')