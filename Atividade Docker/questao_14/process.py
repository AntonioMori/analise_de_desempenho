import pandas as pd
import time

print("Iniciando o processamento de dados...")

data = {
    'Produto': ['Notebook', 'Mouse', 'Teclado'],
    'Preco': [3500.00, 50.00, 150.00]
}

df = pd.DataFrame(data)

time.sleep(2)
print("Processamento concluído: ")
print(df.head())


