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



@app.get('/')
async def root():
    return { 'message': 'Hello there' }



@app.get('/verify')
async def verify():
    url = config['endpoint'] + 'user/tokens/verify'
    req = requests.get(url, headers=headers)
    return req.json()



@app.get('/keys')
async def keys(prefix):
    url = [
        config['endpoint'],
        'accounts/' + config['account'],
        '/storage/kv/namespaces/' + config['namespace'],
        '/keys',
        '?prefix=' + prefix if prefix else ''
    ]
    
    req = requests.get(''.join(url), headers=headers)
    return req.json()
