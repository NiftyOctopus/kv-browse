import requests, json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)



with open('config.json') as config_file:
    config = json.load(config_file)

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




@app.get('/')
async def root():
    return { 'message': 'Hello there' }



@app.get('/verify')
async def verify():
    req = requests.get(urls['verify'], headers=headers)
    return req.json()



@app.get('/keys')
async def keys(prefix):
    url = urls['keys'] + ('?prefix=' + prefix if prefix else '')
    req = requests.get(url, headers=headers)
    return req.json()



@app.get('/value')
async def value(key):
    url = urls['value'] + key
    req = requests.get(url, headers=headers)
    return req.json()



@app.get('/delete')
async def delete(key):
    url = urls['value'] + key
    req = requests.delete(url, headers=headers)
    return req.json()