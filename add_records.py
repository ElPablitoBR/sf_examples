import sqlite3
import random

DB_NAME = "data.db"

def generate_additional_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Lista de países com suas abreviações
    paises = [
        {"code": "AR", "name": "Argentina"},
        {"code": "EC", "name": "Ecuador"},
        {"code": "CL", "name": "Chile"},
        {"code": "PE", "name": "Peru"},
        {"code": "CO", "name": "Colombia"},
        {"code": "MX", "name": "Mexico"},
    ]

    # Gerar 10.000 registros para cada país
    for pais in paises:
        print(f"Adicionando registros para {pais['name']}...")
        for i in range(1, 10001):
            ciclo = f"{pais['code']}2024{random.randint(10, 14)}"  # Ciclo aleatório
            cd_consultora = f"CONS{random.randint(1, 100):05d}"  # Consultora duplicada aleatória
            nombre = f"Consultora {random.randint(1, 100)} de {pais['name']}"  # Nome duplicado
            cursor.execute("""
                INSERT INTO GRUPO_MENSURACION_GC (PAIS, CICLO, CD_CONSULTORA, NOMBRE)
                VALUES (?, ?, ?, ?)
            """, (pais["name"], ciclo, cd_consultora, nombre))

    conn.commit()
    conn.close()
    print("Registros adicionados com sucesso!")

if __name__ == "__main__":
    generate_additional_records()
