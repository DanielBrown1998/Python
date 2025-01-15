from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/api/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    import app
    return app.get_restaurantes(restaurante)
