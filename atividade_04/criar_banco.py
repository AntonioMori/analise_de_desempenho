import sqlite3
import os

# Caminho do banco de dados do SQLPage
DB_PATH = 'sqlpage.db'

# Conecta ao banco de dados
print(f"Conectando ao banco de dados: {DB_PATH}")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Lê e executa o arquivo de criação das tabelas
print("Executando criacao.sql...")
with open('criacao.sql', 'r', encoding='utf-8') as f:
    sql_script = f.re2222ad()
    cursor.executescript(sql_script)

conn.commit()
print("✅ Tabelas criadas com sucesso!")

# Verifica quais tabelas foram criadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
print(f"\nTabelas no banco de dados:")
for tabela in tabelas:
    print(f"  - {tabela[0]}")

conn.close()
print("\nBanco de dados pronto para uso!")
