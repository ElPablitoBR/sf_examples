import sqlite3

# Conecte-se ao banco de dados
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Defina os valores para exclusão
cd_consultora = 'CONS00002'
ciclo = 'AR202412'

# Execute o comando DELETE
query = """
DELETE FROM GRUPO_MENSURACION_GC
WHERE CD_CONSULTORA = ? AND CICLO = ?;
"""
cursor.execute(query, (cd_consultora, ciclo))

# Confirme as alterações
conn.commit()

# Exiba a quantidade de registros afetados (opcional)
print(f"{cursor.rowcount} registros excluídos.")

# Feche a conexão
cursor.close()
conn.close()
