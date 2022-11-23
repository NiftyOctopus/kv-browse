# KV Browse
Simple UI to search and browse Cloudflare KV storage

## Setup
`cd kv-browse/api`  

**Create a Python virtual environment**  
`python3 -m venv benv`  
`source env/bin/activate`  

**Install dependencies**  
`pip install -r requirements.txt`

**Create your config**  
Copy the config.json.example file to config.json  
Enter your info  
Token is refering to Cloudflare [API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

## Usage
`cd kv-browse/api`  

**Activate the virtual environment**  
`source env/bin/activate`  

**Start the local server**  
`uvicorn main:app --reload`
