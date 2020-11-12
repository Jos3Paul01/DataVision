# # OBS: BANCO CRIADO APARTADO PELO SQLITE 

import sqlite3 
import sys

#conexao banco de dados
con = sqlite3.connect('DataVision.db')
Cursor = con.cursor()


#busca arquivo
arq = open('C:/vesao_1_0_23/DataVision/Resultados.txt', 'r')

# verificação de arquivo 
# for linha in arq:
#     print(linha)
# arq.close()


#  INSERE VALORES NA TABELA
con.executemany("insert into DataSet(Detectado,Acuracia) values (?,?)",(arq,))
