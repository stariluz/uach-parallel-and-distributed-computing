import sqlite3
import requests
import threading
import time

# Crear la tabla con los campos definidos
def create_table():
    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        title TEXT,
        first_name TEXT,
        last_name TEXT,
        street_number INTEGER,
        street_name TEXT,
        city TEXT,
        state TEXT,
        country TEXT,
        postcode TEXT,
        latitude TEXT,
        longitude TEXT,
        timezone_offset TEXT,
        timezone_description TEXT,
        email TEXT,
        uuid TEXT,
        username TEXT,
        password TEXT,
        salt TEXT,
        md5 TEXT,
        sha1 TEXT,
        sha256 TEXT,
        dob_date TEXT,
        dob_age INTEGER,
        registered_date TEXT,
        registered_age INTEGER,
        phone TEXT,
        cell TEXT,
        id_name TEXT,
        id_value TEXT,
        picture_large TEXT,
        picture_medium TEXT,
        picture_thumbnail TEXT,
        nat TEXT,
        seed TEXT,
        results INTEGER,
        page INTEGER,
        version TEXT
    );
    ''')
    conn.commit()
    conn.close()

# Función para hacer una solicitud a la API y almacenar el resultado
def fetch_and_store():
    try:
        response = requests.get('https://randomuser.me/api/')
        if response.status_code == 200:
            data = response.json()
            store_response(data)
        else:
            print(f"Error en la solicitud: {response.status_code}")
    except Exception as e:
        print(f"Error en la solicitud: {e}")

# Almacenar la respuesta en la base de datos
def store_response(data):
    user = data['results'][0]  # Obtenemos el primer resultado
    info = data['info']

    conn = sqlite3.connect('responses.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (
        gender, title, first_name, last_name, street_number, street_name, city, state, country, postcode, 
        latitude, longitude, timezone_offset, timezone_description, email, uuid, username, password, salt, md5, sha1, sha256, 
        dob_date, dob_age, registered_date, registered_age, phone, cell, id_name, id_value, picture_large, 
        picture_medium, picture_thumbnail, nat, seed, results, page, version
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
    ''', (
        user['gender'], user['name']['title'], user['name']['first'], user['name']['last'], 
        user['location']['street']['number'], user['location']['street']['name'], user['location']['city'], 
        user['location']['state'], user['location']['country'], user['location']['postcode'], 
        user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude'], 
        user['location']['timezone']['offset'], user['location']['timezone']['description'], 
        user['email'], user['login']['uuid'], user['login']['username'], user['login']['password'], 
        user['login']['salt'], user['login']['md5'], user['login']['sha1'], user['login']['sha256'], 
        user['dob']['date'], user['dob']['age'], user['registered']['date'], user['registered']['age'], 
        user['phone'], user['cell'], user['id']['name'], user['id']['value'], 
        user['picture']['large'], user['picture']['medium'], user['picture']['thumbnail'], 
        user['nat'], info['seed'], info['results'], info['page'], info['version']
    ))

    conn.commit()
    conn.close()

# Función para manejar los threads
def thread_request():
    threads = []
    for _ in range(2):  # 5 requests simultáneas
        thread = threading.Thread(target=fetch_and_store)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Programa principal
if __name__ == '__main__':
    create_table()  # Crear la tabla si no existe
    while True:
        thread_request()
        time.sleep(10)  # Esperar 10 segundos antes de hacer más requests
