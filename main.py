from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DB_NAME = "data.db"

# Configurar arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Conexão com o banco de dados
def get_db_connection():
    return sqlite3.connect(DB_NAME)

# Rota principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Carregar países disponíveis
    cursor.execute("SELECT DISTINCT PAIS FROM GC_CICLO_PAIS")
    paises = [row[0] for row in cursor.fetchall()]

    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "paises": paises})

# Rota para carregar ciclos
@app.get("/ciclos/")
async def get_ciclos(pais: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obter ciclos baseados no país selecionado
    cursor.execute("SELECT CICLO FROM GC_CICLO_PAIS WHERE PAIS = ?", (pais,))
    ciclos = [row[0] for row in cursor.fetchall()]

    conn.close()
    return ciclos

# Rota para carregar grupos
@app.get("/grupos/")
async def get_grupos(pais: str, ciclo: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obter grupos com base em país e ciclo
    cursor.execute("""
        SELECT CD_CONSULTORA, NOMBRE
        FROM GRUPO_MENSURACION_GC
        WHERE PAIS = ? AND CICLO = ?
    """, (pais, ciclo))
    grupos = [{"cd_consultora": row[0], "nombre": row[1]} for row in cursor.fetchall()]

    conn.close()
    return grupos

# Adicionar execução automática ao rodar o script
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8095, reload=True)
