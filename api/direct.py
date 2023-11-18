# Sandbox for interacting with KV directly with Python
import requests, json, time


with open('config.json') as config_file:
    config = json.load(config_file)


def load_list(filename):
    with open(filename + '.txt') as file:
        return [line.rstrip('\n') for line in file]


def save_list(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')


def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


headers = {
    'Content-Type':  'application/json',
    'Authorization': 'Bearer ' + config['token']
}

urls = {
    'verify': config['endpoint'] + 'user/tokens/verify',
    'namespace': ''.join([
        config['endpoint'],
        'accounts/' + config['account'],
        '/storage/kv/namespaces/' + config['namespace'][config['namespace']['use']]
    ])
}

urls['keys']  = urls['namespace'] + '/keys'
urls['value'] = urls['namespace'] + '/values/'


def verify_token():
    req = requests.get(urls['verify'], headers=headers)
    res = req.json()
    print(res)


def get_keys(prefix):
    url  = urls['keys'] + ('?prefix=' + prefix if prefix else '')
    req  = requests.get(url, headers=headers)
    res  = req.json()
    data = res['result']
    return [item['name'] for item in data if 'name' in item]


def get_value(key):
    url = urls['value'] + key
    req = requests.get(url, headers=headers)
    return req.json()


def save_value(key):
    value = get_value(key)
    save_json(value, f'records/{key}.json')
