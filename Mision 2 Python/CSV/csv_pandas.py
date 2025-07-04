import pandas as pd

df = pd.read_csv("cinema.csv")
print(df['Age'])
columnas_a_imprimir = ['Ticket_ID', 'Age', 'Ticket_Price']
df_selec = df[columnas_a_imprimir]
print(df_selec)