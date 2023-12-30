from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return"hi"

@app.get('/api')
def api_root():
    return 'api'