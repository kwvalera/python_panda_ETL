#My first ETL using pandas library in python

#Extract

import pandas as pd

df = pd.read_csv('musicas.csv')
df = df.to_dict()
print(df)

#Transform

def switch(number):
  match number:
    case 0:
      df_copy = df.copy()
      print("\n", df_copy)
      coluna = input("\nDigite a coluna que deseja modificar: ")
      linha = int(input("\nDigite a linha a qual deseja modificar: "))
      novo_valor = input("Digite novo valor: ")
      df_copy[coluna][linha] = novo_valor
      return df_copy
    case default:
      return "Obrigado por usar nosso sistema :)"

number = int(input('Escolha\n0 para editar a planilha\n Outro para sair: '))
df_copy = switch(number)
print(df_copy)

#Load

print("Planilha modificada:")
print(df_copy)

decisao = input("Confirma a modificação? s/n ")

if (decisao == 's'):
  df = pd.DataFrame.from_dict(df_copy)
  df.to_csv('musicas.csv')
else:
  df_copy = df